"""
WSGI config for info project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os

env_name = os.path.basename(os.path.normpath(os.path.dirname(os.path.abspath(__file__))))
env_settings = env_name + ".settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", env_settings)

import sys
sys.path.insert(0, '/home/welkere/python')
sys.path.insert(0, '/home/welkere/python/dev_info')

#print "\n\n\n\n"
#for param in os.environ.keys():
#    print "%30s %s" % (param,os.environ[param])

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
