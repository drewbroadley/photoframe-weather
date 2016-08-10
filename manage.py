#!/usr/bin/env python
import os
import sys

#import pydevd
""" Setup Debugging """
#pydevd.settrace('10.0.2.2', port=60566, stdoutToServer=True, stderrToServer=True)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "photoframe_weather.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
