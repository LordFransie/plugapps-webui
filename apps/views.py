from django.shortcuts import render_to_response
from django.http import HttpRequest
import os
import privateapi.core

def render(filename,**variables):
    context = globals()
    context.update(variables)
    from gluon.template import render
    return render(filename=os.path.join(request.folder,'views',filename),
                  path=os.path.join(request.folder,'views'),
                  context=context,delimiters=('{%','%}'))

def index(request): 
    installed_apps = os.listdir("/etc/installed_apps/")
    return render_to_response('apps/index.html', { "installed_apps": installed_apps })

def package(request):
    package_name = request.GET['name']
    return HttpRequest('apps/' + package_name + '.html')