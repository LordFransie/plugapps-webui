from django.http import HttpResponse
from django.utils import simplejson

import privateapi
import privateapi.core 
import privateapi.pacman
import privateapi.minidlna
import privateapi.samba

from django.contrib.auth.decorators import login_required

import urllib, os
	
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
def dirlist(request):
   r=['<ul class="jqueryFileTree" style="display: none;">']
   try:
       returnvalue = ['<ul class="jqueryFileTree" style="display: none;">']
       directory = urllib.unquote(request.POST['dir'])
       
       for file in os.listdir(directory):
           fullpath = os.path.join(directory,file)
           if os.path.isdir(fullpath):
               returnvalue.append('<li class="directory collapsed"><a href="#" rel="%s/">%s</a></li>' % (fullpath,file))
           else:
               extension = os.path.splitext(file)[1][1:] # get .ext and remove dot
               returnvalue.append('<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (extension,fullpath,file))
       returnvalue.append('</ul>')
   except Exception,exception:
       returnvalue.append('Could not load directory: %s' % str(exception))
   returnvalue.append('</ul>')
   return HttpResponse(''.join(returnvalue))


def jsondirlist(request):
	dirdict = dict()
	#directory = urllib.unquote(request.POST['dir'])
	directory = urllib.unquote('/media/')
	for file in os.listdir(directory):
		currentfile = {}
		fullpath = os.path.join(directory,file)
		if os.path.isdir(fullpath):
			currentfile['directory'] = True
			currentfile['path'] = fullpath
			currentfile['name'] = file
			currentfile['extension'] = False
		else:
			extension = os.path.splitext(file)[1][1:] # get .ext and remove dot
			currentfile['directory'] = False
			currentfile['path'] = fullpath
			currentfile['name'] = file
			currentfile['extension'] = extension
		dirdict[currentfile['name']] = currentfile
	return HttpResponse(simplejson.dumps(dirdict),content_type = 'application/javascript; charset=utf8')