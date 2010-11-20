from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
	(r'^api/', include('api.urls')),
	(r'^system/', include('system.urls')),
	(r'^files/', include('files.urls')),
	(r'^apps/', include('apps.urls')),
	(r'^$', 'home.views.index'),
)
