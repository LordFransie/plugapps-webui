from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
	(r'^create$', 'users.views.create', {}, 'createuser'),
	(r'^delete$', 'users.views.delete', {}, 'deleteuser'),
	(r'^show', 'users.views.index', {}, 'showusers'),
	(r'^$', redirect_to, {'url': '/users/show'}),
)
