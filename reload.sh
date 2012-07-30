!#/bin/bash

clear;
#rm info.db;
#python manage.py syncdb --noinput;
#chmod 666 info.db;

python manage.py sqlclear web_resources | python manage.py dbshell;
python manage.py syncdb;
python manage.py loaddata data/category_fixture.xml
python load_data.py
