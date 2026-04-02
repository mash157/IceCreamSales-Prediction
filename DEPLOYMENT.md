# Deployment Guide - Render.com

This guide will help you deploy the Ice Cream Sales Prediction app on Render.com.

## 📋 Prerequisites

1. **GitHub Account** - Repository already pushed
2. **Render.com Account** - Free at https://render.com
3. **GitHub Repository** - Already set up at https://github.com/mash157/IceCreamSales-Prediction

## 🚀 Step-by-Step Deployment

### Step 1: Connect GitHub to Render

1. Go to [Render.com](https://render.com)
2. Click **Sign Up** or **Sign In**
3. Choose **Sign up with GitHub** for easier connection
4. Authorize Render to access your GitHub repositories

### Step 2: Create a New Web Service

1. Click **New +** button (top-right corner)
2. Select **Web Service**
3. Under "Connect a repository", find and select:
   - Repository: `IceCreamSales-Prediction`
   - Branch: `main`
4. Click **Connect**

### Step 3: Configure the Web Service

Fill in the following details:

| Setting | Value |
|---------|-------|
| **Name** | `icecream-sales-prediction` (or your choice) |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `cd app && gunicorn -w 2 -b 0.0.0.0:$PORT run:app` |
| **Plan** | Free (or Starter for better performance) |

### Step 4: Environment Variables (Optional)

Click **Environment** and add any needed variables:
- `FLASK_ENV=production` (optional - app detects this automatically)

### Step 5: Deploy

1. Click **Create Web Service**
2. Render will:
   - Clone your repository
   - Install dependencies
   - Build the application
   - Deploy it to a live URL

3. **Wait for deployment** (Usually 2-3 minutes)

## ✅ Deployment Complete!

Once deployed, you'll get a URL like:
```
https://icecream-sales-prediction.onrender.com
```

Your app is now **live and accessible** from anywhere!

---

## 📊 Files Used for Deployment

These files were added for Render compatibility:

1. **Procfile** - Tells Render how to start the app
   ```
   web: cd app && gunicorn -w 2 -b 0.0.0.0:$PORT run:app
   ```

2. **runtime.txt** - Specifies Python version
   ```
   python-3.12.0
   ```

3. **requirements.txt** - Updated with gunicorn
   - Flask==3.0.0
   - pandas==2.1.3
   - scikit-learn==1.3.2
   - joblib==1.3.2
   - numpy==1.26.2
   - gunicorn==21.2.0

4. **app/run.py** - Updated to use environment PORT variable

---

## 🔧 Advanced Configuration

### Custom Domain
1. In Render dashboard, go to your service
2. Click **Settings**
3. Under "Custom Domain", enter your domain
4. Follow DNS setup instructions

### Auto-Deploy
- Render automatically deploys when you push to `main` branch
- No additional configuration needed!

### Environment Variables
Add sensitive data via Render dashboard:
1. Your Service → **Environment**
2. Add new environment variables
3. Restart your service

### Logs
View real-time logs:
1. Your Service → **Logs**
2. See all application output and errors

---

## 🐛 Troubleshooting

### Build Fails
- Check `Logs` tab for error messages
- Ensure all dependencies in requirements.txt are correct
- Verify Procfile syntax

### App Crashes on Deploy
- Check logs: Service → **Logs**
- Common issues:
  - Missing environment variables
  - File path issues
  - Model file not found

### Slow Performance
- Upgrade from Free to Starter plan
- Free tier has limited resources
- Starter: $7/month, better performance

### Model Loading Error
- Ensure `model/ice_cream_model.pkl` is committed to Git
- Model files should be small enough for Render's storage

---

## 📈 Monitoring

### Real-time Metrics
1. Go to your service dashboard
2. View **Metrics** tab:
   - CPU usage
   - Memory usage
   - Request rate
   - Response time

### Health Checks
Render performs automatic health checks on your service. If it's unresponsive, it will restart automatically.

---

## 💡 Performance Tips

1. **Use Free Tier for Testing** - Full feature set, limited resources
2. **Upgrade to Starter for Production** - $7/month for better uptime
3. **Monitor Logs Regularly** - Catch issues early
4. **Use Custom Domains** - More professional
5. **Scale as Needed** - Upgrade plan as traffic increases

---

## 🔄 Continuous Deployment

Every time you push to `main` branch:
1. Render detects the change
2. Automatically pulls the latest code
3. Rebuilds the application
4. Deploys the new version (0 downtime)

**To update your app:**
```bash
cd "C:\Users\Admin\Downloads\Icecream sales"
git add -A
git commit -m "Your changes"
git push origin main
```

---

## 📱 Access Your App

Once deployed, access your app at:
```
https://your-service-name.onrender.com
```

Features available:
- ✅ Ice cream sales predictions
- ✅ Real-time statistics
- ✅ Analytics dashboard
- ✅ Beautiful UI with animations
- ✅ Mobile responsive

---

## 🚢 What You Get

- **Automatic HTTPS** (Free SSL)
- **Auto-deploy on push** from GitHub
- **Custom domains** support
- **Environment variables** management
- **Real-time logs**
- **Auto-restart** on crashes
- **Horizontal scaling** (Enterprise)

---

## 📞 Support

For Render issues:
- Visit [Render Documentation](https://docs.render.com/)
- Check Render status page for outages
- Contact Render support via dashboard

For app issues:
- Check logs in Render dashboard
- Review GitHub repository
- Test locally before pushing

---

## Summary

Your Ice Cream Sales Prediction app is now **production-ready** and deployed on Render.com! 🎉

**Deployment is automatic** - just push to GitHub and watch it deploy!

Enjoy your live application! 🍦✨
