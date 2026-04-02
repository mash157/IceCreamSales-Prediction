#!/bin/bash

# Ice Cream Sales ML System - Setup and Run Script
# This script sets up the environment and starts the application

echo ""
echo "========================================================"
echo "Ice Cream Sales ML System - Setup"
echo "========================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Train the model
echo ""
echo "========================================================"
echo "Training Machine Learning Model..."
echo "========================================================"
echo ""
cd model
python3 train_model.py
cd ..

# Start Flask application
echo ""
echo "========================================================"
echo "Starting Flask Web Application"
echo "========================================================"
echo ""
echo "Server will be available at: http://localhost:5000"
echo "Press CTRL+C to stop the server"
echo ""

cd app
python3 run.py
