#! /bin/bash

# Load virtual environment
# source venv/bin/activate
# pipenv shell

# Run Flask application
export FLASK_APP=main.py
flask run --host 0.0.0.0 --port 8080

# deactivate
# exit