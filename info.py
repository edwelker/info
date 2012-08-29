#!/home/welkere/env/dev_info/bin/python

import sys, os

sys.stderr = sys.stdout
#print "Content-type: text/plain"
#print

os.environ['VIRTUAL_ENV'] = '/home/welkere/env/dev_info'

venv = '/home/welkere/env/dev_info/bin/activate_this.py'
execfile(venv, dict(__file__=venv))

_project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#print _project_dir

# Add a custom Python path.
sys.path.insert(0, _project_dir)
sys.path.insert(0, '/home/welkere/python/dev_info')
#need to do this explicitly, since _project_dir is gonna be my staff directory,
#because that's where the cgi is 'running'
sys.path.insert(0, '/home/welkere/python')
sys.path.insert(0, os.path.dirname(_project_dir))

# Switch to the directory of your project. (Optional.)
os.chdir("/home/welkere/python/dev_info")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "dev_info.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
