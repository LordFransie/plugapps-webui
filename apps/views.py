from django.shortcuts import render_to_response
from django.template import RequestContext

import os
import privateapi.core

from django.contrib.auth.decorators import login_required

@login_required
def index(request): 
    installed_apps = os.listdir("/etc/installed_apps/")
    return render_to_response('apps/index.html', { "installed_apps": installed_apps },context_instance=RequestContext(request))

@login_required
def minidlna(request): 
    installed_apps = os.listdir("/etc/installed_apps/")
    return render_to_response('apps/minidlna.html', { "installed_apps": installed_apps },context_instance=RequestContext(request))

@login_required
def samba(request): 
    installed_apps = os.listdir("/etc/installed_apps/")
    return render_to_response('apps/samba.html', { "installed_apps": installed_apps },context_instance=RequestContext(request))


