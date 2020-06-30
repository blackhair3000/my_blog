#!/bin/bash
WORKING_DIR=/root/myenv/virtualenvs/blackhair3000
ACTIVATE_PATH=/root/.virtualenvs/blackhair3000/bin/activate
cd ${WORKING_DIR}
source ${ACTIVATE_PATH}
exec $@


