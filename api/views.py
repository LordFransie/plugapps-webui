from django.http import HttpResponse

import privateapi
import privateapi.core 
import privateapi.pacman
import privateapi.users
import privateapi.minidlna
import privateapi.samba

def create_user(request):
	username = request.post_vars.username
	email = request.post_vars.email
	password = request.post_vars.password
	return HttpResponse(privateapi.users.create())
	

def isinstalled(request,package):
	if getattr(privateapi, package).is_installed():
		return HttpResponse('True')
	return HttpResponse('False')
   
 
def isrunning(request,package):
	if getattr(privateapi, package).is_running():
		return HttpResponse('True')
	return HttpResponse('False')
    
 
def startapp(request,package):
	if getattr(privateapi, package).start():
		return HttpResponse('True')
	return HttpResponse('False')
    
 
def stopapp(request,package):
	if getattr(privateapi, package).stop():
		return HttpResponse('True')
	return HttpResponse('False')
    
 
def getappconfig(request,package):
    return HttpResponse(getattr(privateapi, package).get_app_config())

 
def setappconfig(request,package):
    return HttpResponse(getattr(privateapi, package).set_app_config())
    

def doupdateos(request):
    return HttpResponse(privateapi.pacman.doupdateos())
    

def listupgrades(request):
    return HttpResponse(privateapi.pacman.list_upgrades())
    

def hasupgrades(request):
    return HttpResponse(privateapi.pacman.check())
    
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
	
def rebootnow(request):
    return HttpResponse(privateapi.core.rebootnow())
	
def reloadcode(request):
	return HttpResponse(privateapi.dev.reloadcode())

def diskuse(request):
    return HttpResponse(privateapi.core.getdiskuse())

def loadavg(request):
    return HttpResponse(privateapi.core.getloadavg())

def entropy(request):
    return HttpResponse(privateapi.core.getentropy())

def uptime(request):
    return HttpResponse(privateapi.core.getuptime())

def memory_total(request):
    return HttpResponse(privateapi.core.getmemory_total())


def memory_free(request):
    return HttpResponse(privateapi.core.getmemory_free())
    
    
def memory_percent(request):
    return HttpResponse(privateapi.core.getmemory_percent())