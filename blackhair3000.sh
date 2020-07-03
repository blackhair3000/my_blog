#!/bin/bash
WORKING_DIR=/root/myenv/virtualenvs/blackhair3000
ACTIVATE_PATH=/root/.virtualenvs/blackhair3000/bin/activate
cd ${WORKING_DIR}
source ${ACTIVATE_PATH}
gunicorn --workers 3 --bind unix:/tmp/blackhair3000.com.socket blackhair3000.wsgi:application
exec $@


