#!/usr/bin/env python
import os
import sys

env_name = os.path.basename(os.path.normpath(os.path.dirname(os.path.abspath(__file__))))
env_settings = env_name + ".settings"

sys.path.insert(0, '/home/welkere/python')
sys.path.insert(0, '/home/welkere/python/dev_info')

if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dev_info.settings")
    os.environ['DJANGO_SETTINGS_MODULE'] = env_settings
    
    from django.core.management import execute_from_command_line
    
    for key in os.environ:
        print "%30s %s" % (key, os.environ[key])

    execute_from_command_line(sys.argv)
