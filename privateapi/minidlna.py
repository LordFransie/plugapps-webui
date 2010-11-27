#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket, os, fileinput

def is_installed():
    fpath = "/usr/sbin/minidlna"
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
           
def is_running():
    fpath = "/var/run/minidlna.pid"
    return os.path.isfile(fpath)

def start():
    if is_installed():
       base_start_command_raw = "sudo /etc/rc.d/minidlna start"
       args = shlex.split(base_start_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       for line in process.stdout.readlines():
            newoutput = line.rstrip('\n')
            if not ":: Starting MiniDLNA UPnP Media Server" in newoutput:
                continue
            elif ":: Starting MiniDLNA UPnP Media Server" in newoutput:
                return True
       return False
    else:
        return False

def stop():
    if is_installed():
       base_stop_command_raw = "sudo /etc/rc.d/minidlna stop"
       args = shlex.split(base_stop_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       for line in process.stdout.readlines():
            newoutput = line.rstrip('\n')
            if not ":: Stopping MiniDLNA UPnP Media Server" in newoutput:
                continue
            elif ":: Stopping MiniDLNA UPnP Media Server" in newoutput:
                return True
       return False
    else:
        return False
	
def get_config(file="/etc/minidlna.conf", delim='='):
	d = {}

	if file is None:
		return -1

	for line in fileinput.input(file):
		if not line.strip(): # skip empty or space padded lines
			continue
		if re.compile('^#').search(line) is not None: # skip commented lines
			continue
		else: # pick up key and value pairs
			kvp = line.strip().split(delim)
			if kvp[1].strip().split('#') is not None:
				d[kvp[0].strip()] = kvp[1].split('#')[0].strip()
			else:
				d[kvp[0].strip()] = kvp[1].strip()
	if d['strict_dlna'] == 'no':
		d['strict_dlna'] = False
	else:
		d['strict_dlna'] = True
	if d['enable_tivo'] == 'no':
		d['enable_tivo'] = False
	else:
		d['enable_tivo'] = True		
	
	return d
		
