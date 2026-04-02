"""
Flask Backend for Ice Cream Sales ML Prediction
"""

from flask import Flask, render_template, request, jsonify
import os
import sys
import json
from pathlib import Path

# Add model directory to path
model_dir = os.path.join(os.path.dirname(__file__), '..', 'model')
sys.path.insert(0, model_dir)

from train_model import IceCreamSalesModel

# Initialize Flask app
app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'))

# Initialize ML model
ml_model = IceCreamSalesModel()

# Global variable to store model loaded status
model_loaded = False

def load_model_on_startup():
    """Load the trained model on startup"""
    global model_loaded
    try:
        model_path = os.path.join(model_dir, 'ice_cream_model.pkl')
        if os.path.exists(model_path):
            ml_model.load_model()
            model_loaded = True
            print("✓ ML Model loaded successfully")
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        model_loaded = False


@app.route('/')
def home():
    """Home page - serves the web UI"""
    return render_template('index.html')


@app.route('/api/predict', methods=['POST'])
def predict():
    """API endpoint for predictions"""
    try:
        if not model_loaded:
            return jsonify({
                'error': 'Model not loaded. Please train the model first.',
                'success': False
            }), 400
        
        data = request.get_json()
        
        # Validate input
        if not data or 'temperature' not in data or 'rainfall' not in data:
            return jsonify({
                'error': 'Missing required fields: temperature, rainfall',
                'success': False
            }), 400
        
        try:
            temperature = float(data['temperature'])
            rainfall = float(data.get('rainfall', 0))
        except (ValueError, TypeError):
            return jsonify({
                'error': 'Invalid input types. Temperature and rainfall must be numbers.',
                'success': False
            }), 400
        
        # Validate temperature range
        if temperature < -50 or temperature > 150:
            return jsonify({
                'error': 'Temperature out of reasonable range (-50°F to 150°F)',
                'success': False
            }), 400
        
        if rainfall < 0 or rainfall > 10:
            return jsonify({
                'error': 'Rainfall out of reasonable range (0 to 10 inches)',
                'success': False
            }), 400
        
        # Make prediction
        prediction = ml_model.predict(temperature, rainfall)
        
        return jsonify({
            'success': True,
            'temperature': temperature,
            'rainfall': rainfall,
            'predicted_sales': prediction,
            'unit': 'ice creams'
        }), 200
    
    except Exception as e:
        return jsonify({
            'error': f'Prediction error: {str(e)}',
            'success': False
        }), 500


@app.route('/api/model-info', methods=['GET'])
def model_info():
    """Get model information"""
    if not model_loaded:
        return jsonify({
            'error': 'Model not loaded',
            'success': False
        }), 400
    
    info = ml_model.get_model_info()
    
    return jsonify({
        'success': True,
        'model': info
    }), 200


@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """Get model training metrics"""
    try:
        metrics_path = os.path.join(model_dir, 'metrics.json')
        if os.path.exists(metrics_path):
            with open(metrics_path, 'r') as f:
                metrics = json.load(f)
            return jsonify({
                'success': True,
                'metrics': metrics
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Metrics file not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'success': False
    }), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'success': False
    }), 500


if __name__ == '__main__':
    # Load model on startup
    load_model_on_startup()
    
    # Run Flask dev server
    print("\n" + "="*60)
    print("Ice Cream Sales ML System")
    print("="*60)
    print(f"Server running at http://localhost:5000")
    print("Press CTRL+C to stop the server")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000, host='0.0.0.0')
