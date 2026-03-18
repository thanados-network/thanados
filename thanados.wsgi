import sys
import os
import site

venv_site_packages = '/var/www/frontend/devill/.venv/lib/python3.13/site-packages'
site.addsitedir(venv_site_packages)

path = '/var/www/frontend/devill'
if path not in sys.path:
    sys.path.insert(0, path)

from thanados import app as application
