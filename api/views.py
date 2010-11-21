from django.http import HttpResponse

import privateapi
import privateapi.core 
import privateapi.pacman
import privateapi.users

def create_user(request):
	username = request.post_vars.username
	email = request.post_vars.email
	password = request.post_vars.password
	return HttpResponse(privateapi.users.create())
	

def isinstalled(request):
    package_name = request.get_vars.name
    return HttpResponse(getattr(privateapi, package_name).is_installed())
   
 
def isrunning(request):
    package_name = request.get_vars.name
    return HttpResponse(getattr(privateapi, package_name).is_running())
    
 
def startapp(request):
    package_name = request.get_vars.name
    return HttpResponse(getattr(privateapi, package_name).start())
    
 
def stopapp(request):
    package_name = request.get_vars.name
    return HttpResponse(getattr(privateapi, package_name).stop()) 
    
 
def getappconfig(request):
    package_name = request.get_vars.name
    return HttpResponse(getattr(privateapi, package_name).get_app_config())

 
def setappconfig(request):
    package_name = request.get_vars.name
    return HttpResponse(getattr(privateapi, package_name).set_app_config())
    

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