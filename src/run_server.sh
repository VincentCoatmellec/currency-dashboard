#!/usr/bin/env bash
# go to the directory of the script, so that it can be run from anywhere
cd "$(dirname "$0")" || exit 1

# command to run the Django development server
../venv/bin/python3 manage.py runserver