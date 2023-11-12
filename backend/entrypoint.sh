#!/bin/sh

PYTHONPATH=. python3 src/db.py
exec "$@"
