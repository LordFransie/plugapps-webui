#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket

def mounted_devices():
    base_df_command_raw = "df"
    args = shlex.split(base_df_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    mount_list = []
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        if "Filesystem" in newoutput:
            continue
        elif "udev" in newoutput:
            continue
        elif "shm" in newoutput:
            continue
        else:
            components = newoutput.split()
            mount_list.append(components[0])
    return mount_list

def get_fs_for_device(device):
    base_df_command_raw = "mount"
    args = shlex.split(base_df_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        if device in newoutput:
            components = newoutput.split()
            return components[4]
        else:
            return "Couldn't determine"
    
 
def mount_details():
    base_df_command_raw = "df"
    args = shlex.split(base_df_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    mount_detail_list = []
    counter = 1
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        if "Filesystem" in newoutput:
            continue
        elif "udev" in newoutput:
            continue
        elif "shm" in newoutput:
            continue
        else:
            components = newoutput.split()
            components.append(counter)
            components.append(get_fs_for_device(components[0]))
            mount_detail_list.append(components)
        counter = counter +1
    return mount_detail_list

def rebootnow():
       reboot_command_raw = "reboot"
       args = shlex.split(reboot_command_raw)
       process = subprocess.Popen(args)
       return "Done"

def getcurrentip():
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       s.connect(("plugapps.com",80))
       currentip_tuple = s.getsockname()
       return currentip_tuple[0]

def getkernelversion():
       kernv_cmd = "uname -rv"
       args = shlex.split(kernv_cmd)
       kernv_process = subprocess.Popen(args,stdout=subprocess.PIPE)
       return kernv_process.stdout.read().rstrip('\n')

def getdevicename():
       devicename_cmd = "uname -i"
       args = shlex.split(devicename_cmd)
       devicename_process = subprocess.Popen(args,stdout=subprocess.PIPE)
       return devicename_process.stdout.read()

def getprocessor():
       proc_cmd = "uname -p"
       args = shlex.split(proc_cmd)
       proc_process = subprocess.Popen(args,stdout=subprocess.PIPE)
       return proc_process.stdout.read()

def getarchitecture():
       arch_cmd = "uname -m"
       args = shlex.split(arch_cmd)
       arch_process = subprocess.Popen(args,stdout=subprocess.PIPE)
       return arch_process.stdout.read()

def getdiskuse():
    cmd = """df -h | grep -e ubi0 | awk '{ print $5 }'"""
    process = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    diskuse = process.stdout.read()
    return diskuse

def getloadavg():
     try:
         f = open( "/proc/loadavg" )
         loadavg = shlex.split(f.read())
         f.close()
     except:
        return "Cannot open loadavg file: /proc/loadavg"
     return loadavg[0] + ", " + loadavg[1] + ", " + loadavg[2]

def getentropy():
    cmd = "cat /proc/sys/kernel/random/entropy_avail"
    args = shlex.split(cmd)
    process = subprocess.Popen(args,stdout=subprocess.PIPE)
    entropy = process.stdout.read()
    return entropy

def getuptime():
 
     try:
         f = open( "/proc/uptime" )
         contents = f.read().split()
         f.close()
     except:
        return "Cannot open uptime file: /proc/uptime"
 
     total_seconds = float(contents[0])
 
     # Helper vars:
     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24
 
     # Get the days, hours, etc:
     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
 
     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days> 0:
         string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
     if len(string)> 0 or hours> 0:
         string += str(hours) + (hours == 1 and "h" or "h" ) + ":"
     if len(string)> 0 or minutes> 0:
         string += str(minutes) + (minutes == 1 and "m" or "m")
 
     return string;


def getmemory_total():
      re_parser = re.compile(r'^(?P<key>\S*):\s*(?P<value>\d*)\s*kB' )

      result = dict()
      for line in open('/proc/meminfo'):
           match = re_parser.match(line)
           if not match:
                continue # skip lines that don't parse
           key, value = match.groups(['key', 'value'])
           result[key] = int(value)
      return int(result.get("MemTotal")) / 1024


def getmemory_free():
	cmd = """free | grep cache: | awk '{ print $4 }'"""
	process = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
	freekb = process.stdout.read()
	return int(freekb) / 1024
    
    
def getmemory_percent():
      megabytes_total = getmemory_total()
      megabytes_free = getmemory_free()
      megabytes_used = megabytes_total - megabytes_free
      percent_pre = float(megabytes_free) / float(megabytes_total)
      percent_used = int((percent_pre *100))
      return percent_used

def get_leds():
	f = open( "/proc/cpuinfo", 'r' )
	for line in f.readlines():
		if "DockStar" in line:
			return get_duck_leds()
		else:
			return get_sheeva_leds()
	f.close()

def set_led(led,trigger):
	f = open( "/proc/cpuinfo", 'r' )
	for line in f.readlines():
		if "DockStar" in line:
			return set_duck_led(led,trigger)
	return set_sheeva_led(led,trigger)
	f.close()	



def get_duck_leds():
	duckleds = dict()
	duckleds['green_trigger'] = 'unknown'
	duckleds['orange_trigger'] = 'unknown'
	duckleds['green_status'] = 'unknown'
	duckleds['orange_status'] = 'unknown'
	try:
		f = open( "/sys/class/leds/dockstar:orange:misc/trigger", 'r' )
		for trigger in shlex.split(f.read()):
			if not "[" in trigger:
				continue
			duckleds['orange_trigger'] = trigger.strip('[').strip(']')   
		f.close()
		
		f = open( "/sys/class/leds/dockstar:orange:misc/brightness", 'r' )
		if not "0" in f.read():
			duckleds['orange_status'] = 'on'
		else:
			duckleds['orange_status'] = 'off'
		f.close()
	except:
		pass	
		
	try:
		f = open( "/sys/class/leds/dockstar:green:health/trigger", 'r' )
		for trigger in shlex.split(f.read()):
			if not "[" in trigger:
				continue
			duckleds['green_trigger'] = trigger.strip('[').strip(']')  
		f.close()
		
		f = open( "/sys/class/leds/dockstar:green:health/brightness", 'r' )
		if not "0" in f.read():
			duckleds['green_status'] = 'on'
		else:
			duckleds['green_status'] = 'off'
		f.close()
	except:
		pass
		
	return duckleds
	
def set_duck_led(led,trigger):
	try:
		if led == 'orange':
			f = open( "/sys/class/leds/dockstar:orange:misc/trigger", 'w' )
			f.write(trigger)
		elif led == 'green':
			f = open( "/sys/class/leds/dockstar:green:health/trigger", 'w' )
			f.write(trigger)
		f.close()
	except:
		return False
	return True
	
def get_sheeva_leds():
	sheevaleds = dict()
	sheevaleds['green_trigger'] = 'unknown'
	try:
		f = open( "/sys/class/leds/plug:green:health/trigger", 'r' )
		for trigger in shlex.split(f.read()):
			if not "[" in trigger:
				continue
			sheevaleds['green_trigger'] = trigger.strip('[').strip(']')   
		f.close()
	except:
		pass	
	return sheevaleds

def set_sheeva_led(led,trigger):
	try:
		if led == 'orange':
			f = open( "/sys/class/leds/plug:orange:misc/trigger", 'w' )
			f.write(trigger)
		elif led == 'green':
			f = open( "/sys/class/leds/plug:green:health/trigger", 'w' )
			f.write(trigger)
		f.close()
	except:
		return False
	return True