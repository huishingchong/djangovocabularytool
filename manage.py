#!usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vocabularytool.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Coulnd't import Django. Are you sure it's installed "
            "and available on your PYTHONPATH environment variable? Did you forget to activate virtual environment"
    ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()