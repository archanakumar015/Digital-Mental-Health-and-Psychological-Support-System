#!/usr/bin/env python
"""
Simple test to verify Django setup is working correctly.
"""
import os
import sys
import django

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curacore.settings')

try:
    # Setup Django
    django.setup()
    
    # Import Django components to test
    from django.conf import settings
    from django.core.management import execute_from_command_line
    
    print("✓ Django setup successful!")
    print(f"✓ Secret key configured: {'SECRET_KEY' in os.environ or settings.SECRET_KEY}")
    print(f"✓ Database configured: {settings.DATABASES['default']['ENGINE']}")
    print(f"✓ Installed apps: {len(settings.INSTALLED_APPS)} apps")
    print(f"✓ REST Framework configured: {'rest_framework' in settings.INSTALLED_APPS}")
    print(f"✓ JWT configured: {'rest_framework_simplejwt' in settings.INSTALLED_APPS}")
    print(f"✓ CORS configured: {'corsheaders' in settings.INSTALLED_APPS}")
    print(f"✓ API docs configured: {'drf_spectacular' in settings.INSTALLED_APPS}")
    
    print("\nDjango foundation setup is complete and working!")
    
except Exception as e:
    print(f"✗ Error in Django setup: {e}")
    sys.exit(1)