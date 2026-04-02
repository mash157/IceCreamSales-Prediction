"""
WSGI entry point for Gunicorn
Imports the Flask app from app/run.py
"""

import sys
import os

# Add app directory to path
app_dir = os.path.join(os.path.dirname(__file__), 'app')
sys.path.insert(0, app_dir)

# Import the Flask app instance
from run import app

if __name__ == '__main__':
    app.run()
