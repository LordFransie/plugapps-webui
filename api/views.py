from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

import privateapi
import privateapi.core 
import privateapi.pacman
import privateapi.minidlna
import privateapi.samba

from django.contrib.auth.decorators import login_required

import urllib, os, shutil, mimetypes, traceback, sys
	
@login_required
def isinstalled(request,package):
	if getattr(privateapi, package).is_installed():
		return HttpResponse('True')
	return HttpResponse('False')
   
@login_required
def isrunning(request,package):
	if getattr(privateapi, package).is_running():
		return HttpResponse('True')
	return HttpResponse('False')
    
@login_required 
def startapp(request,package):
	if getattr(privateapi, package).start():
		return HttpResponse('True')
	return HttpResponse('False')
    
@login_required 
def stopapp(request,package):
	if getattr(privateapi, package).stop():
		return HttpResponse('True')
	return HttpResponse('False')
    
@login_required 
def getappconfig(request,package):
    return HttpResponse(getattr(privateapi, package).get_app_config())

@login_required 
def setappconfig(request,package):
	return HttpResponse(getattr(privateapi, package).set_app_config())
    
@login_required
def doupdateos(request):
    return HttpResponse(privateapi.pacman.doupdateos())
    
@login_required
def listupgrades(request):
    return HttpResponse(privateapi.pacman.list_upgrades())
    
@login_required
def hasupgrades(request):
    return HttpResponse(privateapi.pacman.check())

@login_required    
def checkforupdates(request):
	hasupdates = privateapi.pacman.check()
	if hasupdates:
		updatelist = privateapi.pacman.list_upgrades()
		response = "System updates found:<br/><br/>"
		for package in updatelist:
			response += '<p class="packagename">'
			response += package
			response += '</p><br/>'
		return HttpResponse(response)
	else:
		return HttpResponse("No updates found")

@login_required	
def rebootnow(request):
    return HttpResponse(privateapi.core.rebootnow())

@login_required
def diskuse(request):
    return HttpResponse(privateapi.core.getdiskuse())

@login_required
def loadavg(request):
    return HttpResponse(privateapi.core.getloadavg())

@login_required
def entropy(request):
    return HttpResponse(privateapi.core.getentropy())

@login_required
def uptime(request):
    return HttpResponse(privateapi.core.getuptime())

@login_required
def memory_total(request):
    return HttpResponse(privateapi.core.getmemory_total())


@login_required
def memory_free(request):
    return HttpResponse(privateapi.core.getmemory_free())
    
@login_required    
def memory_percent(request):
    return HttpResponse(privateapi.core.getmemory_percent())

@login_required	
@csrf_exempt
def fileapi(request):
	def nodot(item): 
		return item[0] != '.'
		
	if request.method == 'POST':
		if request.POST['cmd'] == 'get':
			dirs = []
			directory = '/media/' + urllib.unquote(request.POST['path'])
			for file in filter(nodot, os.listdir(directory)):
				currentfile = {}
				fullpath = os.path.join(directory,file)
				if os.path.isdir(fullpath):
					currentfile['fullpath'] = fullpath
					currentfile['directory'] = directory
					currentfile['text'] = file
					currentfile['iconCls'] = 'folder'
					currentfile['leaf'] = False
					currentfile['disabled'] = False
				else:
					extension = os.path.splitext(file)[1][1:] # get .ext and remove dot
					currentfile['fullpath'] = fullpath
					currentfile['directory'] = directory
					currentfile['text'] = file
					currentfile['iconCls'] = 'file-' + extension
					currentfile['leaf'] = True
					currentfile['disabled'] = False
				dirs.append(currentfile)
			return HttpResponse(simplejson.dumps(dirs),content_type = 'application/javascript; charset=utf8')
			
		if request.POST['cmd'] == 'rename':
				response = dict()
				oldname = '/media/' + urllib.unquote(request.POST['oldname'])
				newname = '/media/' + urllib.unquote(request.POST['newname'])
				if os.path.exists(oldname):
					try:
						os.rename(oldname,newname)
						response['success'] = True
					except:
						response['success'] = False
						response['error'] = 'Cannot rename file %s to %s' %(oldname,newname)
				else:
					response['success'] = False
					response['error'] = 'Cannot rename file %s to %s' %(oldname,newname)
				return HttpResponse(simplejson.dumps(response),content_type = 'application/javascript; charset=utf8')
				
		if request.POST['cmd'] == 'newdir':
			response = dict()
			dir = '/media/' + urllib.unquote(request.POST['dir'])
			try:
				os.mkdir(dir)
				response['success'] = True
			except:
				response['success'] = False
				response['error'] = 'Cannot create directory: %s' %(dir)
			return HttpResponse(simplejson.dumps(response),content_type = 'application/javascript; charset=utf8')
					
		if request.POST['cmd'] == 'delete':
			response = dict()
			path = '/media/' + urllib.unquote(request.POST['file'])
			if os.path.isdir(path):
				try:
					shutil.rmtree(path)
					response['success'] = True
				except:
					response['success'] = False
					response['error'] = 'Cannot delete directory: %s' %(path)
			else:
				try:
					os.remove(path)
					response['success'] = True
				except:
					response['success'] = False
					response['error'] = 'Cannot delete file: %s' %(path)
			return HttpResponse(simplejson.dumps(response),content_type = 'application/javascript; charset=utf8')
			


		if request.POST['cmd'] == 'download':
			path = '/media/' + urllib.unquote(request.POST['path'])
			try:
				f = open( path , 'rb' )
				mimetype = mimetypes.guess_type(f.name)
				response = HttpResponse(f.read(), mimetype='%s' % mimetype[0])
				response['Content-Length'] = f.tell()
				response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(f.name)
			except:
				(exc_type, exc_info, tb) = sys.exc_info()
				tracebackstring = ''
				for tb in traceback.format_tb(tb):
					tracebackstring += "%s\n" % tb
				response = HttpResponse("Cannot download file: %s\n\n %s" % (path,tracebackstring))
			return response
			
			
			
			