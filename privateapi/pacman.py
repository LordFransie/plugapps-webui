#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket

def check():
    base_pacmansyup_command_raw = "sudo pacman -Syup"
    args = shlex.split(base_pacmansyup_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    output_list = []
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        if not "there is nothing to do" in newoutput:
            continue
        elif "there is nothing to do" in newoutput:
            return False
    return True
           
def list_upgrades():
    base_pacmanqu_command_raw = "sudo pacman -Qu"
    args = shlex.split(base_pacmanqu_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    output_list = []
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        output_list.append(newoutput)
    return output_list

def doupdateos():
       base_update_command_raw = "sudo pacman -Syu --noconfirm --noprogressbar"
       args = shlex.split(base_update_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       output_list = []
       for line in process.stdout.readlines():
              newoutput = line.rstrip('\n')
              output_list.append(newoutput)
              output_list.append('<br/>')
       return output_list
