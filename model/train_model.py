"""
Ice Cream Sales ML Model Training
Predicts ice cream sales based on temperature and other features
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os
import json
from datetime import datetime

class IceCreamSalesModel:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.feature_names = ['Temperature', 'Rainfall']
        self.target_name = 'IceCreamsSold'
        self.model_dir = os.path.join(os.path.dirname(__file__))
        
    def load_and_preprocess_data(self, csv_path):
        """Load CSV data and preprocess it"""
        print(f"Loading data from {csv_path}...")
        df = pd.read_csv(csv_path)
        
        # Handle missing values
        print("Handling missing values...")
        df = df.dropna()
        
        # Feature selection
        X = df[self.feature_names].values
        y = df[self.target_name].values
        
        # Normalize features
        print("Normalizing features...")
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)
        
        print(f"Data shape: {X_scaled.shape}")
        print(f"Target shape: {y.shape}")
        
        return X_scaled, y
    
    def train(self, csv_path, train_split=0.7, test_split=0.3):
        """Train the linear regression model"""
        X, y = self.load_and_preprocess_data(csv_path)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_split, random_state=42
        )
        
        print(f"Training set size: {X_train.shape[0]}")
        print(f"Test set size: {X_test.shape[0]}")
        
        # Train model
        print("Training linear regression model...")
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        
        # Evaluate
        print("\nModel Evaluation:")
        y_pred_train = self.model.predict(X_train)
        y_pred_test = self.model.predict(X_test)
        
        mae_train = mean_absolute_error(y_train, y_pred_train)
        mae_test = mean_absolute_error(y_test, y_pred_test)
        r2_train = r2_score(y_train, y_pred_train)
        r2_test = r2_score(y_test, y_pred_test)
        
        print(f"Training MAE: {mae_train:.4f}")
        print(f"Testing MAE: {mae_test:.4f}")
        print(f"Training R²: {r2_train:.4f}")
        print(f"Testing R²: {r2_test:.4f}")
        
        metrics = {
            'mae_train': float(mae_train),
            'mae_test': float(mae_test),
            'r2_train': float(r2_train),
            'r2_test': float(r2_test),
            'training_samples': int(X_train.shape[0]),
            'test_samples': int(X_test.shape[0]),
            'trained_on': datetime.now().isoformat()
        }
        
        return metrics
    
    def save_model(self, model_name='ice_cream_model.pkl'):
        """Save trained model and scaler"""
        model_path = os.path.join(self.model_dir, model_name)
        scaler_path = os.path.join(self.model_dir, 'scaler.pkl')
        
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)
        
        print(f"Model saved to {model_path}")
        print(f"Scaler saved to {scaler_path}")
        
        return model_path, scaler_path
    
    def load_model(self, model_name='ice_cream_model.pkl'):
        """Load saved model and scaler"""
        model_path = os.path.join(self.model_dir, model_name)
        scaler_path = os.path.join(self.model_dir, 'scaler.pkl')
        
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        
        print(f"Model loaded from {model_path}")
        return True
    
    def predict(self, temperature, rainfall):
        """Predict ice cream sales for given temperature and rainfall"""
        if self.model is None or self.scaler is None:
            raise ValueError("Model not trained or loaded")
        
        # Prepare input
        input_data = np.array([[temperature, rainfall]])
        input_scaled = self.scaler.transform(input_data)
        
        # Predict
        prediction = self.model.predict(input_scaled)[0]
        
        # Ensure non-negative prediction
        prediction = max(0, prediction)
        
        return round(prediction, 2)
    
    def get_model_info(self):
        """Get model information"""
        if self.model is None:
            return None
        
        return {
            'model_type': 'Linear Regression',
            'features': self.feature_names,
            'target': self.target_name,
            'coefficients': dict(zip(self.feature_names, self.model.coef_.tolist())),
            'intercept': float(self.model.intercept_),
            'scaler_mean': self.scaler.mean_.tolist() if self.scaler else None,
            'scaler_std': self.scaler.scale_.tolist() if self.scaler else None
        }


def main():
    """Main execution"""
    # Initialize model
    ml_model = IceCreamSalesModel()
    
    # Path to CSV file
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'ice_cream_sales.csv')
    
    # Train model
    metrics = ml_model.train(csv_path)
    
    # Save model
    ml_model.save_model()
    
    # Save metrics
    metrics_path = os.path.join(os.path.dirname(__file__), 'metrics.json')
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    print(f"\nMetrics saved to {metrics_path}")
    print("\nModel training complete!")


if __name__ == '__main__':
    main()
