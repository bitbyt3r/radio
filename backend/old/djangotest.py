#!/afs/umbc.edu/public/web/sites/wmbc/dev/htdocs/backend/venv/bin/python
import auth
import cgitb
import cgi
cgitb.enable()
import django

print "Content-Type: text/html\n\n"
print "Django verions information:"
print django.get_version()
