#!/afs/umbc.edu/users/m/a/mark25/home/wmbc/dev/htdocs/backend/venv/bin/python
import sys, os
sys.path.insert(0, "/afs/umbc.edu/users/m/a/mark25/home/wmbc/dev/cgi-bin/backend")
os.environ['DJANGO_SETTINGS_MODULE'] = "backend.settings"
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
