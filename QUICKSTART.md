# Quick Start Guide

## 🚀 Getting Started in 3 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Train the Model
```bash
cd model
python train_model.py
cd ..
```

You should see output like:
```
Loading data from ../data/ice_cream_sales.csv...
Handling missing values...
Normalizing features...
Data shape: (277, 2)
Target shape: (277,)
Training set size: 194
Test set size: 83
Training linear regression model...

Model Evaluation:
Training MAE: 12.53
Testing MAE: 13.47
Training R²: 0.8945
Testing R²: 0.8762

Model saved to /path/to/ice_cream_model.pkl
Scaler saved to /path/to/scaler.pkl

Metrics saved to metrics.json
```

### Step 3: Start the Web Server
```bash
cd app
python run.py
```

You should see:
```
============================================================
Ice Cream Sales ML System
============================================================
Server running at http://localhost:5000
Press CTRL+C to stop the server
============================================================
```

### Step 4: Open in Browser
Visit: **http://localhost:5000**

---

## 📝 Using the Application

### Making a Prediction
1. Adjust the **Temperature** slider (50°F - 100°F)
2. Adjust the **Rainfall** slider (0 - 2 inches)
3. Or type values directly in the input fields
4. Click **"Predict Sales"**
5. View results with insights

### Understanding Results
- **Predicted Sales**: Number of ice creams expected to sell
- **Input Conditions**: Temperature and rainfall used
- **Insights**: AI-generated advice based on conditions
- **Model Info**: Performance metrics and features

---

## 🔧 Troubleshooting

### Model Not Found Error
**Problem**: "Model not loaded. Please train the model first."
**Solution**:
```bash
cd model
python train_model.py
cd ..
```

### Port 5000 Already in Use
**Problem**: "Port 5000 is already in use"
**Solution**:
- Close other applications using port 5000
- Or modify the port in `app/run.py` (change line: `app.run(debug=True, port=5000)`)

### Import Errors
**Problem**: "ModuleNotFoundError: No module named 'flask'"
**Solution**:
```bash
pip install -r requirements.txt
```

### No Data Found
**Problem**: "CSV file not found"
**Solution**:
- Ensure `data/ice_cream_sales.csv` exists
- Check file path in `model/train_model.py`

---

## 📁 Project Structure

```
IceCreamSalesML/
├── data/
│   └── ice_cream_sales.csv        # Dataset
├── model/
│   ├── train_model.py              # ML training script
│   ├── ice_cream_model.pkl         # Trained model (after training)
│   ├── scaler.pkl                  # Feature scaler (after training)
│   └── metrics.json                # Performance metrics (after training)
├── app/
│   └── run.py                      # Flask server
├── templates/
│   └── index.html                  # Web interface
├── static/
│   ├── css/style.css               # Styling
│   └── js/main.js                  # JavaScript logic
├── requirements.txt                # Python packages
├── config.py                       # Configuration
├── run.bat / run.sh               # Startup scripts
├── README.md                       # Full documentation
├── PRD.md                          # Product requirements
└── QUICKSTART.md                   # This file
```

---

## 🌐 API Usage

### Make a Prediction via API

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"temperature": 75.5, "rainfall": 0.5}'
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

### Get Model Metrics

```bash
curl http://localhost:5000/api/metrics
```

---

## 💡 Tips & Tricks

### 1. Use Sliders for Exploration
- The sliders provide a visual way to explore the relationship between weather and sales
- Drag left/right to see how predictions change

### 2. Check Model Performance
- Look at R² score (0.85+ is good)
- Lower MAE means better predictions
- Compare train vs test to check for overfitting

### 3. Real Weather Integration
- In production, integrate with weather API
- Automatically populate temperature and rainfall
- Make daily predictions for planning

### 4. Keyboard Shortcuts
- Press **Enter** in temperature field to move to rainfall field
- Press **Enter** in rainfall field to submit prediction

---

## 🚀 Advanced Usage

### Retraining the Model

To use newer data:
```bash
# Update data/ice_cream_sales.csv with new data
# Then:
cd model
python train_model.py
cd ..
```

The API will automatically reload the updated model on next request.

### Custom Configuration

Edit `config.py` to customize:
- Server port (SERVER_PORT)
- Debug mode (DEBUG)
- Input validation ranges
- Feature selection

### Deploying to Production

Using Gunicorn (WSGI server):
```bash
pip install gunicorn
cd app
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

Using Docker:
```bash
docker build -t icecream-ml .
docker run -p 5000:5000 icecream-ml
```

---

## 📊 Example Scenarios

### Scenario 1: Hot & Dry Day
- **Temperature**: 95°F
- **Rainfall**: 0.1 in
- **Expected**: ~200+ ice creams (very high sales)

### Scenario 2: Cool & Rainy Day
- **Temperature**: 60°F
- **Rainfall**: 1.5 in
- **Expected**: ~40-50 ice creams (low sales)

### Scenario 3: Perfect Day
- **Temperature**: 75°F
- **Rainfall**: 0 in
- **Expected**: ~120-130 ice creams (good sales)

---

## 🆘 Getting Help

1. **Check README.md** - Comprehensive documentation
2. **Review PRD.md** - Detailed specifications
3. **Check Model Logs** - Run `python model/train_model.py` for diagnostics
4. **Browser Console** - Press F12 for JavaScript errors
5. **Server Console** - Watch terminal for Flask error messages

---

## ✅ Next Steps

After startup:

- [ ] Try making 3-5 predictions with different weather
- [ ] Check model performance metrics
- [ ] Review the glassmorphism design
- [ ] Test on mobile device
- [ ] Integrate with your business data
- [ ] Plan production deployment

---

**Enjoy using the Ice Cream Sales ML System! 🍦**
