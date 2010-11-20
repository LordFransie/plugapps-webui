from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^storage$', 'system.views.storage', {}, 'storage'),
	(r'^software$', 'system.views.software', {}, 'software'),
	(r'^networking$', 'system.views.networking', {}, 'networking'),
	(r'^reboot$', 'system.views.reboot', {}, 'reboot'),
	(r'^$', 'system.views.index', {}, 'system'),
)
