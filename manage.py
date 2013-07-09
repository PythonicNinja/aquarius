#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, 'aquarius'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'lib'))
    
    if os.path.isfile(os.path.join(PROJECT_ROOT, 'settings', 'local.py')):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aquarius.settings.local")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aquarius.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
