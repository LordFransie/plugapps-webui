from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^samba', 'apps.views.samba', {}, 'samba'),
	(r'^minidlna', 'apps.views.minidlna', {}, 'minidlna'),
	(r'^$', 'apps.views.index', {}, 'apps'),

)
