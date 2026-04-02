# Configuration file for Ice Cream Sales ML System

# Server Configuration
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000
DEBUG = True
DEVELOPMENT = True

# Model Configuration
MODEL_NAME = 'ice_cream_model.pkl'
SCALER_NAME = 'scaler.pkl'
METRICS_FILE = 'metrics.json'

# Model Hyperparameters
TRAIN_TEST_SPLIT = 0.3
RANDOM_STATE = 42

# Features and Target
FEATURES = ['Temperature', 'Rainfall']
TARGET = 'IceCreamsSold'

# Input Validation Ranges
TEMPERATURE_MIN = -50
TEMPERATURE_MAX = 150
RAINFALL_MIN = 0
RAINFALL_MAX = 10

# API Configuration
API_VERSION = '1.0'
JSON_SORT_KEYS = False

# Logging
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# CORS Configuration
CORS_ORIGINS = '*'
CORS_METHODS = ['GET', 'POST']
CORS_ALLOW_HEADERS = ['Content-Type']

# Performance Settings
MAX_REQUEST_SIZE = 1024 * 16  # 16MB
REQUEST_TIMEOUT = 30
PREDICTION_TIMEOUT = 5

# Data Configuration
CSV_ENCODING = 'utf-8'
CSV_SEPARATOR = ','

# Cache Settings
CACHE_TIMEOUT = 3600  # 1 hour
MODEL_CACHE = True
