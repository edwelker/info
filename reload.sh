!#/bin/bash

clear;

export PYTHONPATH="$PYTHONPATH:$(pwd -P):$(dirname $(pwd -P))"

#python manage.py syncdb --noinput;
#chmod 666 info.db;
echo "export the sql to clear, pipe it to dbshell"

python manage.py sqlclear web_resources | python manage.py dbshell;
echo "syncdb"
#python manage.py syncdb;
echo "load the category fixture"
#python manage.py loaddata data/category_fixture.xml
echo "call load_data"
#python load_data.py

export PYTHONPATH=""
