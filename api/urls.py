from django.conf.urls.defaults import *

urlpatterns = patterns('',

	(r'^isinstalled$', 'api.views.isinstalled'),
	(r'^isrunning$', 'api.views.isrunning'),
	(r'^startapp$', 'api.views.startapp'),
	(r'^stopapp$', 'api.views.stopapp'),
	(r'^getappconfig$', 'api.views.getappconfig'),
	(r'^setappconfig$', 'api.views.setappconfig'),
	

	(r'^doupdateos$', 'api.views.doupdateos'),
	(r'^listupgrades$', 'api.views.listupgrades'),
	(r'^hasupgrades$', 'api.views.hasupgrades'),
	(r'^checkforupdates$', 'api.views.checkforupdates'),
	

	(r'^rebootnow$', 'api.views.rebootnow'),
	

	(r'^diskuse$', 'api.views.diskuse'),
	(r'^loadavg$', 'api.views.loadavg'),
	(r'^entropy$', 'api.views.entropy'),
	(r'^uptime$', 'api.views.uptime'),
	(r'^memory_total$', 'api.views.memory_total'),
	(r'^memory_free$', 'api.views.memory_free'),
	(r'^memory_percent$', 'api.views.memory_percent'),
	

	(r'^createuser$', 'api.views.create_user'),
)
