#!/home/welkere/env/info/bin/python

import sys, os

#sys.stderr = sys.stdout
#print "Content-type: text/plain"
#print

os.environ['VIRTUAL_ENV'] = '/home/welkere/env/info'

venv = '/home/welkere/env/info/bin/activate_this.py'
execfile(venv, dict(__file__=venv))

_project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add a custom Python path.
sys.path.insert(0, _project_dir)
sys.path.insert(0, '/home/welkere/python/info')
sys.path.insert(0, os.path.dirname(_project_dir))

# Switch to the directory of your project. (Optional.)
# os.chdir("/home/welkere/qatest")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "info.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
