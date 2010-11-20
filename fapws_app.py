#!/usr/bin/env python

import fapws._evwsgi as evwsgi
from fapws import base
import time
import sys, os
sys.setcheckinterval(100000) # since we don't use threads, internal checks are no more required
from fapws.contrib import django_handler, views


import django

sys.path.append('/opt')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
def start():
    evwsgi.start("0.0.0.0", "80")
    
    evwsgi.set_base_module(base)
    
    def generic(environ, start_response):
        res=django_handler.handler(environ, start_response)
        return [res]
    
    static=views.Staticfile('/opt/webui/static/', maxage=2629000)
    evwsgi.wsgi_cb(("/static/",static))    
    evwsgi.wsgi_cb(('',generic))
    
    evwsgi.set_debug(0)
    evwsgi.run()
    

if __name__=="__main__":
    start()

