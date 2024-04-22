#!/bin/bash

# Apply migrations
python manage.py migrate

# Load data from fixtures

# Start the Gunicorn server
gunicorn --config gunicorn_config.py core.wsgi:application