from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^storage$', 'system.views.storage'),
	(r'^software$', 'system.views.software'),
	(r'^networking$', 'system.views.networking'),
	(r'^reboot$', 'system.views.reboot'),
	(r'^$', 'system.views.index'),
)
