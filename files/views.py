from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render_to_response('files/index.html', {}, context_instance=RequestContext(request))

@login_required	
def browse(request):
    return render_to_response('files/browse.html', {}, context_instance=RequestContext(request))

@login_required
def share(request):
    return render_to_response('files/share.html', {}, context_instance=RequestContext(request))

@login_required
def download(request):
    return HttpResponse("File")

@login_required	
def upload(request):
    return render_to_response('files/upload.html', {}, context_instance=RequestContext(request))
	
	
