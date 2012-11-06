import sys, os

sys.stderr = sys.stdout
#print "Content-type: text/plain"
#print

homedir = '/home/welkere'
#the name of the current directory is the same as the env name
env_name =  os.path.basename(os.path.normpath(os.path.dirname(__file__)))

venv_loc = homedir + '/env/' + env_name
activate_loc = venv_loc + '/bin/activate_this.py'
info_parent_loc = homedir + '/python'
info_loc = info_parent_loc + '/' + env_name
settings = env_name + '.settings'

#print venv_loc
#print activate_loc
#print info_parent_loc
#print info_loc
#print settings

os.environ['VIRTUAL_ENV'] = venv_loc 

venv = activate_loc
execfile(venv, dict(__file__=venv))

#_project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#print _project_dir

# Add a custom Python path.
sys.path.insert(0, info_loc)
sys.path.insert(0, info_parent_loc)

# Switch to the directory of your project. (Optional.)
os.chdir(info_loc)

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = settings

#for param in os.environ.keys():
#    print "%30s %s" % (param,os.environ[param])
 
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")

