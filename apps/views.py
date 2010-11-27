from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django import forms
import os
import privateapi.core
import privateapi.minidlna
import privateapi.samba

class MinidlnaForm(forms.Form):
	strict_dlna = forms.BooleanField()
	enable_tivo = forms.BooleanField()
	#album_art_names = forms.CharField(max_length=300)
	media_dir = forms.CharField()
	serial = forms.CharField()
	port = forms.CharField()


@login_required
def index(request): 
    installed_apps = os.listdir("/etc/installed_apps/")
    return render_to_response('apps/index.html', { "installed_apps": installed_apps },context_instance=RequestContext(request))

@login_required
def minidlna(request): 
	if request.method == 'POST':
		pass
	else:
		installed_apps = os.listdir("/etc/installed_apps/")
		config_dict = privateapi.minidlna.get_config()
		form = MinidlnaForm(initial=config_dict)
		return render_to_response('apps/minidlna.html', { "installed_apps": installed_apps, "form": form },context_instance=RequestContext(request))

@login_required
def samba(request): 
    installed_apps = os.listdir("/etc/installed_apps/")
    return render_to_response('apps/samba.html', { "installed_apps": installed_apps },context_instance=RequestContext(request))


