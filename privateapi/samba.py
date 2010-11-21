#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket, os

def is_installed():
    fpath = "/usr/sbin/smbd"
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
           
def is_running():
    fpath = "/var/run/samba/smbd.pid"
    return os.path.isfile(fpath)

def start():
    if is_installed():
       base_start_command_raw = "sudo /etc/rc.d/samba start"
       args = shlex.split(base_start_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       for line in process.stdout.readlines():
            newoutput = line.rstrip('\n')
            if not ":: Starting Samba Server" in newoutput:
                continue
            elif ":: Starting Samba Server" in newoutput:
                return True
       return False
    else:
        return False

def stop():
    if is_installed():
       base_stop_command_raw = "sudo /etc/rc.d/samba stop"
       args = shlex.split(base_stop_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       for line in process.stdout.readlines():
            newoutput = line.rstrip('\n')
            if not ":: Stopping Samba Server" in newoutput:
                continue
            elif ":: Stopping Samba Server" in newoutput:
                return True
       return False
    else:
        return False
