!#/bin/bash

rm info.db;
python manage.py syncdb --noinput;
python load_data.py
