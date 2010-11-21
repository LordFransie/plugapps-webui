from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def index(request):
	user_list = User.objects.all()
	contents = { "user_list": user_list } 
	return render_to_response('users/index.html', contents, context_instance=RequestContext(request))

def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/users/show")
    else:
        form = UserCreationForm()
    return render_to_response('users/create.html', { 'form': form, }, context_instance=RequestContext(request))
	
def delete(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		user = User.objects.get(username=name)
		user.delete()
		return HttpResponseRedirect("/users/show")
	else:
		return HttpResponseRedirect("/users/show")
	return render_to_response('users/show.html', {}, context_instance=RequestContext(request))