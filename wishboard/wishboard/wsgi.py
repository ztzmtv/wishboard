"""
WSGI config for wishboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

from dotenv import load_dotenv
import os
load_dotenv()

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wishboard.settings')

application = get_wsgi_application()
