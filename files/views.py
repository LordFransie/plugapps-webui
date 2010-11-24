from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import os, shlex,array, urllib

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
	
@login_required
def dirlist(request):
   r=['<ul class="jqueryFileTree" style="display: none;">']
   try:
       r=['<ul class="jqueryFileTree" style="display: none;">']
       d=urllib.unquote(request.POST['dir'])
       
       for f in os.listdir(d):
           ff=os.path.join(d,f)
           if os.path.isdir(ff):
               r.append('<li class="directory collapsed"><a href="#" rel="%s/">%s</a></li>' % (ff,f))
           else:
               e=os.path.splitext(f)[1][1:] # get .ext and remove dot
               r.append('<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (e,ff,f))
       r.append('</ul>')
   except Exception,e:
       r.append('Could not load directory: %s' % str(e))
   r.append('</ul>')
   return HttpResponse(''.join(r))
