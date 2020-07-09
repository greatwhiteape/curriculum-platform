#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    settings = "curriculum_platform.settings.{}"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings.format(os.environ.get('CURRICULUM_ENV')))
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curriculum_platform.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
