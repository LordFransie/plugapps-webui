from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from files.models import Share
from django.core.files.storage import Storage
from django.conf import settings

class PlugStorage(Storage):
	def __init__(self, option=None):
		if not option:
			option = settings.CUSTOM_STORAGE_OPTIONS
			
	def delete():
		pass
		
	def exists():
		pass
		
	def listdir():
		pass
	
	def size():
		pass
		
	def url():
		pass

@login_required
def index(request):
    return render_to_response('files/index.html', {}, context_instance=RequestContext(request))

@login_required	
def browse(request):
    return render_to_response('files/browse.html', {}, context_instance=RequestContext(request))

@login_required
def share(request):
    return render_to_response('files/share.html', {}, context_instance=RequestContext(request))


def download(request):
    fileuuid = request.GET.get('id', '')
	if fileuuid:
		filerecord = Share(uuid=fileuuid)
		response = HttpResponse(, mimetype='application/vnd.ms-excel')
		response['Content-Disposition'] = 'attachment; filename=foo.xls'
    return HttpResponse("Error, not a valid shared file")
	
@login_required
def addshare(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/users/show")
    else:
        form = UserCreationForm()
    return HttpResponse("File")

@login_required	
def upload(request):
    return render_to_response('files/upload.html', {}, context_instance=RequestContext(request))
	
	
