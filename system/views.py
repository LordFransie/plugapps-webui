from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
import privateapi.core
import privateapi.pacman

from django.contrib.auth.decorators import login_required

class LedForm(forms.Form):
	TRIGGER_CHOICES = (
		('none', 'No Trigger'),
		('nand-disk', 'NAND Activity'),
		('mmc0', 'SD Activity'),
		('timer', 'Timer'),
		('heartbeat', 'Heartbeat'),
		('default-on', 'Default on'),
	)
	green_trigger = forms.ChoiceField(choices=TRIGGER_CHOICES)
	orange_trigger = forms.ChoiceField(choices=TRIGGER_CHOICES)

@login_required
def index(request):
	currentip = privateapi.core.getcurrentip()
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
	stats = {"currentip": currentip, "currentuptime": currentuptime, "load": load, "memused": memused, "memfree": memfree, "memtotal": memtotal, "percentused": percentused, "currentip": currentip, "kernelversion": kernelversion, "devicename": devicename, "processor": processor, "architecture": architecture } 
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
	installed_packages = privateapi.pacman.list_installed()
	return render_to_response('system/software.html', { "installed_packages": installed_packages }, context_instance=RequestContext(request))

@login_required
def reboot(request):
	return render_to_response('system/reboot.html', {}, context_instance=RequestContext(request))


@login_required
def leds(request):
	if request.method == 'POST':
		form = LedForm(request.POST)
		if form.is_valid():
			privateapi.core.set_led('green',form.cleaned_data['green_trigger'])
			privateapi.core.set_led('orange',form.cleaned_data['orange_trigger'])
	else:
		led_dict = privateapi.core.get_leds()
		form = LedForm(initial=led_dict)
	return render_to_response('system/leds.html', { "form": form }, context_instance=RequestContext(request))
	