"""
WSGI config for RealTimeColab project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from channels.routing import ProtocolTypeRouter 
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RealTimeColab.settings')

wsgi_app = get_wsgi_application()

application = ProtocolTypeRouter({
    "http": wsgi_app,
    # Just HTTP for now. (We can add other protocols later.)
})