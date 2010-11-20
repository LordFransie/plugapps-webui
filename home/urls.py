from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
	(r'^system$', include('system.urls')),
	(r'^files$', include('files.urls')),
	(r'^apps$', include('apps.urls)),
	(r'^', 'home.views.index'),
)
