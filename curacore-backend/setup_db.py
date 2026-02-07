#!/usr/bin/env python
"""
Script to set up the initial Django database and run migrations.
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curacore.settings')
    
    # Setup Django
    django.setup()
    
    # Run makemigrations
    print("Running makemigrations...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    # Run migrate
    print("Running migrate...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    print("Database setup complete!")