#!/usr/bin/python

# Virtualenv
activate_this = '/home/pi/code/flask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/pi/code/flask/app')

from app import app as application
application.secret_key = 'key1'
