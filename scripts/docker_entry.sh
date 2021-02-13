#!/usr/bin/env bash

# Send SIGTERM to all running processes on exit
trap "/bin/kill -s TERM -1" SIGTERM SIGQUIT

case "$1" in
    '' | 'build')
        (cd src && uvicorn main:app --reload)
    ;;
    'tests')
        (PYTHONPATH=$PYTHONPATH:src pytest tests -vv)
    ;;
    *) exec "${@}" ;;
esac
