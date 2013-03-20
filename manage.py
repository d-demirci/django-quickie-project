#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosite.settings")

    # add "src" dir to sys.path
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
    sys.path.insert(0, src_path)
    # add it to env too so that it survives forks (but only if no PYTHONPATH was set)
    os.environ.setdefault("PYTHONPATH", src_path)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
