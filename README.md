# 🍦 Ice Cream Sales Prediction - ML Web Application

A premium machine learning web application that predicts ice cream sales based on weather conditions using a trained linear regression model. Built with Flask, Scikit-learn, and featuring a modern glassmorphism UI with **bright white premium design** and full mobile responsiveness.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green?logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.2-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

---

## 🌐 Live Demo

**Try it now:** [https://icecreamsales-prediction.onrender.com/](https://icecreamsales-prediction.onrender.com/)

Deployed on Render.com with Python 3.10 and all dependencies optimized for production.

---

## ✨ Features

### 🤖 Machine Learning
- **Linear Regression Model** trained on historical ice cream sales data
- **Model Accuracy**: R² = 0.9888 (98.88% variance explained)
- **Mean Absolute Error**: 4.34 units
- **Features**: Temperature (°F) and Rainfall (inches)
- **Real-time Predictions** with instant results
- **Data from**: April - October 2025 (200 samples)

### 🎨 Premium UI/UX
- **Bright White Premium Theme** with vibrant accent colors
- **Glassmorphism Design** with animated gradient blobs
- **Fully Responsive** - Optimized for mobile, tablet, and desktop
- **5 Mobile Breakpoints** for perfect display on all devices
- **Smooth Animations** and micro-interactions
- **Touch-Friendly Interface** for mobile devices

### 📊 Data Insights & Analytics
- **Real-time Statistics** - Average sales, temperature/rainfall impact
- **Advanced Analytics** - KPI cards with key metrics
- **Correlation Visualization** - Interactive correlation charts
- **Peak Sales Analysis** - Identifies optimal conditions
- **Monthly Trends** - Seasonal pattern analysis
- **Model Performance Display** - R², MAE, and other metrics

### 🌐 Fully Responsive Design
- **Mobile First** approach with adaptive layouts
- **Breakpoints**: Desktop (1024px+), Tablet (768-1023px), Mobile Large (481-767px), Mobile (max 480px)
- **Fluid Typography** that scales with screen size
- **Touch-Optimized** buttons and form inputs
- **100% Mobile Compatible** on all modern devices

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- pip (Python package manager)
- Modern web browser

### Installation

1. **Navigate to project directory**
```bash
cd "C:\Users\Admin\Downloads\Icecream sales"
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Train the model (if needed)**
```bash
cd model
python train_model.py
cd ..
```

4. **Start the Flask server**
```bash
cd app
python run.py
```

5. **Open in browser**
```
http://localhost:5000
```

---

## 📁 Project Structure

```
Icecream sales/
├── data/
│   └── ice_cream_sales.csv          # Training data (200 samples)
├── model/
│   ├── train_model.py               # ML pipeline & training
│   ├── ice_cream_model.pkl          # Trained model
│   ├── scaler.pkl                   # Feature scaler
│   └── metrics.json                 # Model performance
├── app/
│   ├── run.py                       # Flask server
│   └── config.py                    # Configuration
├── templates/
│   └── index.html                   # Main UI
├── static/
│   ├── css/
│   │   └── style.css                # Premium styling (1600+ lines)
│   └── js/
│       └── main.js                  # Client-side logic
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 🤖 Machine Learning Model

### Model Details
- **Algorithm**: Linear Regression
- **Features**: Temperature (°F), Rainfall (inches)
- **Target**: Ice Cream Sales (units)
- **Training Data**: 277 samples
- **Train/Test Split**: 70/30

### Performance
- **MAE (Mean Absolute Error)**: Measures average prediction error in units
- **R² Score**: Indicates how well the model explains variance (0-1)

The model learns the relationship between weather conditions and sales:
- Higher temperatures → More ice cream sales
- Rainy weather → Fewer ice cream sales

### Data Features
```
Date           : Sales date
DayOfWeek      : Day of the week
Month          : Month of the year
Temperature    : Temperature in Fahrenheit
Rainfall       : Rainfall in inches
IceCreamsSold  : Target variable (units sold)
```

## 💻 API Endpoints

### GET /
Returns the web interface.

### POST /api/predict
Makes a prediction for given weather conditions.

**Request:**
```json
{
  "temperature": 75.5,
  "rainfall": 0.5
}
```

**Response:**
```json
{
  "success": true,
  "temperature": 75.5,
  "rainfall": 0.5,
  "predicted_sales": 125,
  "unit": "ice creams"
}
```

### GET /api/model-info
Returns model architecture and coefficients.

### GET /api/metrics
Returns model performance metrics.

## 🎨 UI Features

### Glassmorphism Design
- Frosted glass effect with backdrop blur
- Gradient backgrounds with animated blobs
- Smooth animations and transitions
- Responsive design for all devices

### Interactive Elements
- **Input Sliders**: Drag to adjust temperature and rainfall
- **Real-time Sync**: Inputs sync with sliders
- **Live Validation**: Input validation as you type
- **Visual Feedback**: Animated predictions and insights
- **Performance Display**: Model metrics and information

### Sections
1. **Header**: Title and subtitle with animation
2. **Prediction Form**: Input temperature and rainfall
3. **Results Card**: Displays predictions with insights
4. **Model Info**: Model details and performance metrics
5. **Footer**: Attribution and tech stack

## 🔧 Configuration

### Temperature Range
- Minimum: -50°F
- Maximum: 150°F
- Default: 75°F

### Rainfall Range
- Minimum: 0 inches
- Maximum: 10 inches
- Default: 0.5 inches

### Model Files
Models are saved in the `model/` directory:
- `ice_cream_model.pkl`: Serialized trained model
- `scaler.pkl`: Feature normalizer
- `metrics.json`: Training metrics

## 📊 Data Preprocessing

The training pipeline includes:
1. **Loading**: CSV data ingestion
2. **Cleaning**: Missing value handling
3. **Selection**: Feature selection (Temperature, Rainfall)
4. **Normalization**: StandardScaler for feature scaling
5. **Splitting**: 70% training, 30% testing

## 🧪 Training Process

To retrain the model:

```bash
cd model
python train_model.py
```

This will:
1. Load the data
2. Preprocess features
3. Train the linear regression model
4. Evaluate on test set
5. Save model and scaler
6. Output metrics to metrics.json

## 📈 Model Evaluation

The model is evaluated using:
- **MAE (Mean Absolute Error)**: Average absolute error in predictions
- **R² Score**: Coefficient of determination (0 = poor, 1 = perfect)

View metrics in:
- `model/metrics.json` (after training)
- Web UI (Model Information section)

## 🌐 Deployment

### Local Development
```bash
python app/run.py
```
Uses Flask development server with debug mode.

### Production Deployment
For production, use a WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app.run:app
```

### Docker Deployment
Create a Dockerfile:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app/run.py"]
```

Build and run:
```bash
docker build -t icecream-sales-ml .
docker run -p 5000:5000 icecream-sales-ml
```

## 🛠️ Troubleshooting

### Model Not Loaded
**Error**: "Model not loaded. Please train the model first."
**Solution**: Run `python model/train_model.py` to train the model.

### Port Already in Use
**Error**: "Port 5000 is already in use"
**Solution**: Change port in `app/run.py` or kill the process using port 5000.

### Import Errors
**Error**: "Module not found"
**Solution**: Ensure virtual environment is activated and requirements are installed.

## 📚 Technologies Used

- **Python 3.8+**
- **Flask 3.0**: Web framework
- **Scikit-learn 1.3**: Machine learning
- **Pandas 2.1**: Data processing
- **NumPy 1.26**: Numerical computing
- **Joblib 1.3**: Model serialization
- **HTML5/CSS3/JavaScript**: Frontend

## 🎓 Learning Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)
- [Feature Scaling](https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling)

## 📝 License

This project is provided as-is for educational purposes.

## 👨‍💻 Development

### Adding New Features
1. Train data files in `data/`
2. Update model training in `model/train_model.py`
3. Add API endpoints in `app/run.py`
4. Update UI components in `templates/` and `static/`

### Code Structure
- **Model**: Self-contained ML pipeline
- **API**: RESTful endpoints with error handling
- **Frontend**: Vanilla JavaScript with no dependencies

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review error messages in the console
3. Check model training output
4. Verify data file format and location

## 🚀 Future Enhancements

- [ ] Multiple regression models (Random Forest, Gradient Boosting)
- [ ] Time-series analysis with historical trends
- [ ] Seasonal adjustments
- [ ] Multiple feature inputs (humidity, day of week)
- [ ] Model comparison dashboard
- [ ] Database integration for sales tracking
- [ ] Batch predictions
- [ ] Model retraining scheduler

---

## 📱 Mobile Testing

The application has been optimized and tested on:
- **Desktop**: Chrome, Firefox, Safari, Edge (1920px+)
- **Tablet**: iPad, Android tablets (768px - 1024px)
- **Mobile**: iPhone, Android phones (320px - 767px)
- **Responsive**: Adapts perfectly to any screen size

---

## 🔒 Security Notes

- All input validation is performed
- Model predictions use normalized features
- No user data is stored
- HTTPS recommended for production deployment

---

## 📊 Performance Metrics

- **Prediction Time**: < 100ms
- **Page Load Time**: < 2 seconds
- **API Response Time**: < 200ms
- **CSS Bundle Size**: ~50KB
- **JS Bundle Size**: ~15KB

---

## 🎯 Use Cases

- Ice cream shop sales forecasting
- Weather-based inventory planning
- Revenue prediction
- Marketing strategy optimization
- Business intelligence

---

## 💡 Improvements Made

✅ **Version 2.0 Updates:**
- Bright white premium theme with vibrant gradients
- Full mobile responsiveness (5 breakpoints)
- Enhanced background with mesh pattern and 4 animated blobs
- Developer credit "Developed by @mash157❤️" in footer
- Improved form centering on mobile devices
- Better Touch-friendly interface
- Advanced analytics sections
- Comprehensive responsive testing

---

## 👨‍💻 Developer

**Developed by @mash157❤️**

April 2, 2026

---

## 📄 License

This project is provided for educational and commercial use under the MIT License.

---

## 🙏 Acknowledgments

- Built with **Flask** - Lightweight web framework
- Powered by **Scikit-learn** - Machine learning library
- Data processing with **Pandas** - Data manipulation
- **Glassmorphism** design inspiration
- **Premium UI/UX** best practices

---

**Made with ❤️ using Machine Learning | Flask + Scikit-learn**

**Last Updated**: April 2, 2026
