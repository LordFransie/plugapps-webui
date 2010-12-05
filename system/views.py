from django.shortcuts import render_to_response
from django.template import RequestContext
import privateapi.core
import privateapi.pacman

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	currentuptime = privateapi.core.getuptime() 
	load = privateapi.core.getloadavg()
	memfree = privateapi.core.getmemory_free() 
	memtotal = privateapi.core.getmemory_total()
	memused = str(int(memtotal) - int(memfree))
	percentused = str(100 - int(privateapi.core.getmemory_percent()))
	currentip = privateapi.core.getcurrentip()
	kernelversion = privateapi.core.getkernelversion()
	devicename = privateapi.core.getdevicename()
	processor = privateapi.core.getprocessor()
	architecture = privateapi.core.getarchitecture()
	stats = {"currentuptime": currentuptime, "load": load, "memused": memused, "memfree": memfree, "memtotal": memtotal, "percentused": percentused, "currentip": currentip, "kernelversion": kernelversion, "devicename": devicename, "processor": processor, "architecture": architecture } 
	return render_to_response('system/index.html', stats, context_instance=RequestContext(request))

@login_required
def storage(request):
	mounted_device_list = privateapi.core.mounted_devices()
	mounted_device_details = privateapi.core.mount_details()
	number_of_mounts = len(mounted_device_list)
	stats = { "mounted_device_list": mounted_device_list, "mounted_device_details": mounted_device_details, "number_of_mounts": number_of_mounts }
	return render_to_response('system/storage.html', stats, context_instance=RequestContext(request))

@login_required   
def networking(request):
	currentip = privateapi.core.getcurrentip()
	stats = { "currentip": currentip }
	return render_to_response('system/networking.html', stats, context_instance=RequestContext(request))
    
@login_required  
def software(request):
	return render_to_response('system/software.html', {}, context_instance=RequestContext(request))

@login_required
def reboot(request):
	return render_to_response('system/reboot.html', {}, context_instance=RequestContext(request))
