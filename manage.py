#!/usr/bin/env python
"""Django's command-line utility for administrative taskss."""
import os
import sys
from dotenv import read_dotenv


def main():
    """Run administrative tasks."""
    read_dotenv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management.commands.runserver import Command as runserver
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    runserver.default_addr = os.environ.get('DJANGO_HOST')
    runserver.default_port = os.environ.get('DJANGO_PORT')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
