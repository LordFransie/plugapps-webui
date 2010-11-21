from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to


urlpatterns = patterns('',
	(r'^storage$', 'system.views.storage', {}, 'storage'),
	(r'^users$', 'system.views.users', {}, 'users'),
	(r'^software$', 'system.views.software', {}, 'software'),
	(r'^networking$', 'system.views.networking', {}, 'networking'),
	(r'^reboot$', 'system.views.reboot', {}, 'reboot'),
	(r'^about', 'system.views.index', {}, 'system'),
	(r'^$', redirect_to, {'url': '/system/about'}),
)
