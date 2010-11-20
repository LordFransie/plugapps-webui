from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^samba', 'apps.views.samba'),
	(r'^minidlna', 'apps.views.minidlna'),
	(r'^$', 'apps.views.index'),

)
