"""
WSGI config for mytv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
# MUST come before the bellow import!!!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytv.settings")

from dj_static import Cling
application = Cling(get_wsgi_application())
