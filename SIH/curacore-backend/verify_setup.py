#!/usr/bin/env python
"""
Verification script for Django setup.
This script checks if all components are properly configured.
"""
import os
import sys

def main():
    """Verify Django setup."""
    print("🔍 Verifying CuraCore Django Backend Setup...")
    print("=" * 50)
    
    # Check if manage.py exists
    if os.path.exists('manage.py'):
        print("✓ manage.py found")
    else:
        print("✗ manage.py not found")
        return False
    
    # Check if settings.py exists
    if os.path.exists('curacore/settings.py'):
        print("✓ settings.py found")
    else:
        print("✗ settings.py not found")
        return False
    
    # Check if urls.py exists
    if os.path.exists('curacore/urls.py'):
        print("✓ urls.py found")
    else:
        print("✗ urls.py not found")
        return False
    
    # Check if requirements.txt exists
    if os.path.exists('requirements.txt'):
        print("✓ requirements.txt found")
    else:
        print("✗ requirements.txt not found")
        return False
    
    # Try to import Django settings
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curacore.settings')
        import django
        django.setup()
        from django.conf import settings
        print("✓ Django settings loaded successfully")
        
        # Check key configurations
        required_apps = [
            'rest_framework',
            'rest_framework_simplejwt', 
            'corsheaders',
            'drf_spectacular'
        ]
        
        for app in required_apps:
            if app in settings.INSTALLED_APPS:
                print(f"✓ {app} configured")
            else:
                print(f"✗ {app} not configured")
                return False
        
        # Check database configuration
        if 'default' in settings.DATABASES:
            print("✓ Database configured")
        else:
            print("✗ Database not configured")
            return False
            
        # Check JWT configuration
        if hasattr(settings, 'SIMPLE_JWT'):
            print("✓ JWT authentication configured")
        else:
            print("✗ JWT authentication not configured")
            return False
            
        # Check CORS configuration
        if hasattr(settings, 'CORS_ALLOWED_ORIGINS'):
            print("✓ CORS configured")
        else:
            print("✗ CORS not configured")
            return False
            
    except Exception as e:
        print(f"✗ Error loading Django settings: {e}")
        return False
    
    print("=" * 50)
    print("🎉 Django backend foundation setup is COMPLETE!")
    print("\nNext steps:")
    print("1. Run: python manage.py makemigrations")
    print("2. Run: python manage.py migrate")
    print("3. Run: python manage.py runserver")
    print("4. Visit: http://localhost:8000/health/ to test")
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)