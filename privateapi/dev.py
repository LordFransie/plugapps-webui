#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket

def reloadcode():
    base_reload_command_raw = "sudo /etc/rc.d/webui restart"
    args = shlex.split(base_reload_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    return True
