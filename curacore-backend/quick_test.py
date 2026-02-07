import os
import sys

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curacore.settings')

try:
    import django
    django.setup()
    print("Django setup successful!")
    
    from django.conf import settings
    print(f"Database: {settings.DATABASES['default']['ENGINE']}")
    print(f"Installed apps: {len(settings.INSTALLED_APPS)}")
    
except Exception as e:
    print(f"Error: {e}")