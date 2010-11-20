from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^dirlist$', 'files.views.dirlist'),
	(r'^browse', 'files.views.browse', {}, 'browse'),
	(r'^share', 'files.views.share', {}, 'share'),
	(r'^$', 'files.views.index', {}, 'files'),
)
