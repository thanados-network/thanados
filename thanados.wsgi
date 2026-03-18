import sys
import os

BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

VENV_PACKAGES = os.path.join(BASE_DIR, '.venv/lib/python3.13/site-packages')
if os.path.exists(VENV_PACKAGES):
    import site
    site.addsitedir(VENV_PACKAGES)

from thanados import app as application
