"""
ASGI config for charity_site_from_students_hackathon_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charity_site_from_students_hackathon_project.settings')

application = get_asgi_application()
