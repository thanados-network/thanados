import sys
import os

path = '/var/www/frontend/devill'
if path not in sys.path:
    sys.path.insert(0, path)

from thanados import app as application
