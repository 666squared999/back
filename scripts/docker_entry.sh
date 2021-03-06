#!/usr/bin/env bash

# Send SIGTERM to all running processes on exit
trap "/bin/kill -s TERM -1" SIGTERM SIGQUIT

case "$1" in
    '' | 'build')
        (cd src && python3 manage.py makemigrations && python3 manage.py migrate && uwsgi --http :8000 --wsgi-file src/wsgi.py)
    ;;
    'tests')
        (PYTHONPATH=$PYTHONPATH:src pytest tests -vv)
    ;;
    *) exec "${@}" ;;
esac
