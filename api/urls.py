from django.conf.urls.defaults import *

urlpatterns = patterns('',

	(r'^isinstalled/(?P<package>\w{1,50})/$', 'api.views.isinstalled'),
	(r'^isrunning/(?P<package>\w{1,50})/$', 'api.views.isrunning'),
	(r'^startapp/(?P<package>\w{1,50})/$', 'api.views.startapp'),
	(r'^stopapp/(?P<package>\w{1,50})/$', 'api.views.stopapp'),
	(r'^getappconfig/(?P<package>\w{1,50})/$', 'api.views.getappconfig'),
	(r'^setappconfig/(?P<package>\w{1,50})/$', 'api.views.setappconfig'),
	

	(r'^doupdateos$', 'api.views.doupdateos'),
	(r'^listupgrades$', 'api.views.listupgrades'),
	(r'^hasupgrades$', 'api.views.hasupgrades'),
	(r'^checkforupdates$', 'api.views.checkforupdates'),
	

	(r'^rebootnow$', 'api.views.rebootnow'),
	
	(r'^dirlist$', 'api.views.dirlist'),
	(r'^jsondirlist$', 'api.views.jsondirlist'),
	

	(r'^diskuse$', 'api.views.diskuse'),
	(r'^loadavg$', 'api.views.loadavg'),
	(r'^entropy$', 'api.views.entropy'),
	(r'^uptime$', 'api.views.uptime'),
	(r'^memory_total$', 'api.views.memory_total'),
	(r'^memory_free$', 'api.views.memory_free'),
	(r'^memory_percent$', 'api.views.memory_percent'),
	
)
