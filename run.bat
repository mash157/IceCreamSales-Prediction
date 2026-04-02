@echo off
REM Ice Cream Sales ML System - Setup and Run Script
REM This script sets up the environment and starts the application

setlocal enabledelayedexpansion

echo.
echo ========================================================
echo Ice Cream Sales ML System - Setup
echo ========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Train the model
echo.
echo ========================================================
echo Training Machine Learning Model...
echo ========================================================
echo.
cd model
python train_model.py
cd ..

REM Start Flask application
echo.
echo ========================================================
echo Starting Flask Web Application
echo ========================================================
echo.
echo Server will be available at: http://localhost:5000
echo Press CTRL+C to stop the server
echo.

cd app
python run.py

pause
