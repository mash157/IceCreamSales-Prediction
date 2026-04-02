// DOM Elements
const form = document.getElementById('predictionForm');
const temperatureInput = document.getElementById('temperature');
const rainfallInput = document.getElementById('rainfall');
const tempRange = document.getElementById('tempRange');
const rainRange = document.getElementById('rainRange');
const resultsSection = document.getElementById('resultsSection');
const errorSection = document.getElementById('errorSection');
const errorMessage = document.getElementById('errorMessage');
const clearBtn = document.getElementById('clearBtn');
const predictionValue = document.getElementById('predictionValue');
const resultTemp = document.getElementById('resultTemp');
const resultRain = document.getElementById('resultRain');
const insightText = document.getElementById('insightText');
const trainingInfo = document.getElementById('trainingInfo');
const metricMAE = document.getElementById('metricMAE');
const metricMAETrain = document.getElementById('metricMAETrain');
const metricR2 = document.getElementById('metricR2');
const metricR2Train = document.getElementById('metricR2Train');

// Sync range sliders with input fields
tempRange.addEventListener('input', (e) => {
    temperatureInput.value = e.target.value;
});

temperatureInput.addEventListener('input', (e) => {
    let value = parseFloat(e.target.value);
    if (value < -50) value = -50;
    if (value > 150) value = 150;
    tempRange.value = value;
});

rainRange.addEventListener('input', (e) => {
    rainfallInput.value = e.target.value;
});

rainfallInput.addEventListener('input', (e) => {
    let value = parseFloat(e.target.value);
    if (value < 0) value = 0;
    if (value > 10) value = 10;
    rainRange.value = value;
});

// Form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    await predictSales();
});

// Clear results
clearBtn.addEventListener('click', () => {
    resultsSection.classList.add('hidden');
    form.reset();
    temperatureInput.focus();
});

/**
 * Make prediction API call
 */
async function predictSales() {
    const temperature = parseFloat(temperatureInput.value);
    const rainfall = parseFloat(rainfallInput.value);

    // Validate inputs
    if (isNaN(temperature) || isNaN(rainfall)) {
        showError('Please enter valid temperature and rainfall values');
        return;
    }

    if (temperature < -50 || temperature > 150) {
        showError('Temperature must be between -50°F and 150°F');
        return;
    }

    if (rainfall < 0 || rainfall > 10) {
        showError('Rainfall must be between 0 and 10 inches');
        return;
    }

    // Hide error section
    errorSection.classList.add('hidden');

    // Show loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    const btnContent = submitBtn.querySelector('.btn-content');
    const btnLoader = submitBtn.querySelector('.btn-loader');
    btnContent.classList.add('hidden');
    btnLoader.classList.remove('hidden');
    submitBtn.disabled = true;

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                temperature: temperature,
                rainfall: rainfall
            })
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            showError(data.error || 'Prediction failed');
            return;
        }

        // Display results
        displayResults(temperature, rainfall, data.predicted_sales);

    } catch (error) {
        showError(`Error: ${error.message}`);
    } finally {
        // Hide loading state
        btnContent.classList.remove('hidden');
        btnLoader.classList.add('hidden');
        submitBtn.disabled = false;
    }
}

/**
 * Display prediction results
 */
function displayResults(temperature, rainfall, prediction) {
    resultTemp.textContent = `${temperature}°F`;
    resultRain.textContent = `${rainfall} in`;
    predictionValue.textContent = Math.round(prediction);

    // Generate insight
    const insight = generateInsight(temperature, rainfall, prediction);
    insightText.textContent = insight;
    insightText.style.whiteSpace = 'pre-wrap';  // Preserve line breaks

    // Show results section
    resultsSection.classList.remove('hidden');
    
    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

/**
 * Generate insight based on prediction
 */
function generateInsight(temperature, rainfall, prediction) {
    let insight = '';
    let weatherCondition = '';
    let recommendation = '';

    // Weather analysis
    if (temperature < 50) {
        weatherCondition = 'Cold weather significantly reduces ice cream demand. ';
    } else if (temperature < 65) {
        weatherCondition = 'Cool weather shows moderate ice cream sales. ';
    } else if (temperature < 80) {
        weatherCondition = 'Pleasant temperature drives steady ice cream sales. ';
    } else {
        weatherCondition = 'Hot weather creates strong demand for ice cream. ';
    }

    // Rainfall impact
    if (rainfall > 1.5) {
        weatherCondition += 'Heavy rain will significantly decrease customer foot traffic.';
    } else if (rainfall > 0.75) {
        weatherCondition += 'Moderate rain may reduce customer visits.';
    } else if (rainfall > 0.3) {
        weatherCondition += 'Light rain has minimal impact on sales.';
    } else {
        weatherCondition += 'Clear weather encourages outdoor activities and sales.';
    }

    insight += weatherCondition + ' ';

    // Sales forecast recommendation
    if (prediction > 180) {
        recommendation = '🚀 PEAK SALES: Stock maximum inventory. Plan extra staff. High profit margin day expected.';
    } else if (prediction > 140) {
        recommendation = '📈 STRONG SALES: Good day ahead. Adequate staffing recommended. Stock moderately high.';
    } else if (prediction > 100) {
        recommendation = '📊 MODERATE SALES: Normal operations. Standard inventory levels recommended.';
    } else if (prediction > 60) {
        recommendation = '📉 SLOW SALES: Consider promotional activities. Stock minimally to avoid waste.';
    } else {
        recommendation = '❄️ VERY SLOW: Plan accordingly. Minimize inventory. Focus on premium/specialty items.';
    }

    return insight + '\n\n' + recommendation;
}

/**
 * Show error message
 */
function showError(message) {
    errorMessage.textContent = message;
    errorSection.classList.remove('hidden');
    errorSection.scrollIntoView({ behavior: 'smooth' });
}

/**
 * Load model information and metrics
 */
async function loadModelInfo() {
    try {
        // Load metrics
        const metricsResponse = await fetch('/api/metrics');
        const metricsData = await metricsResponse.json();

        if (metricsData.success && metricsData.metrics) {
            const metrics = metricsData.metrics;
            trainingInfo.textContent = `${metrics.training_samples} samples`;
            metricMAE.textContent = metrics.mae_test.toFixed(2);
            metricMAETrain.textContent = metrics.mae_train.toFixed(2);
            metricR2.textContent = (metrics.r2_test * 100).toFixed(2) + '%';
            metricR2Train.textContent = (metrics.r2_train * 100).toFixed(2) + '%';
            
            // Update accuracy value
            const accuracyValue = document.getElementById('accuracyValue');
            if (accuracyValue) {
                accuracyValue.textContent = (metrics.r2_test * 100).toFixed(2) + '%';
            }
        }
    } catch (error) {
        console.error('Error loading model info:', error);
        trainingInfo.textContent = 'Unable to load';
    }
}

/**
 * Load and display data statistics
 */
async function loadDataStatistics() {
    try {
        // Simulated statistics based on the training data
        // In production, these would come from the backend
        const statistics = {
            avgSales: 120,
            tempCoeff: 2.8,
            rainCoeff: -35.2,
            highestSales: 252,
            lowestSales: 15,
            monthlyAverage: 123
        };

        // Update stat cards
        const statAvgSales = document.getElementById('statAvgSales');
        const statTempCoeff = document.getElementById('statTempCoeff');
        const statRainCoeff = document.getElementById('statRainCoeff');

        if (statAvgSales) statAvgSales.textContent = statistics.avgSales;
        if (statTempCoeff) statTempCoeff.textContent = '+' + statistics.tempCoeff.toFixed(1);
        if (statRainCoeff) statRainCoeff.textContent = statistics.rainCoeff.toFixed(1);

        // Animate values on load
        animateStatValues();

    } catch (error) {
        console.error('Error loading statistics:', error);
    }
}

/**
 * Animate statistics values on load
 */
function animateStatValues() {
    const statValues = document.querySelectorAll('.stat-value, .analytics-value, .metric-value');
    statValues.forEach((element, index) => {
        element.style.animation = `slideInUp 0.6s ease ${index * 0.1}s both`;
    });
}

/**
 * Format number with commas
 */
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

/**
 * Initialize page
 */
document.addEventListener('DOMContentLoaded', () => {
    // Load model information and statistics
    loadModelInfo();
    loadDataStatistics();

    // Set default values
    temperatureInput.value = 75;
    rainfallInput.value = 0.5;
    tempRange.value = 75;
    rainRange.value = 0.5;

    // Focus on temperature input
    temperatureInput.focus();
});

/**
 * Add keyboard support
 */
document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && document.activeElement === temperatureInput) {
        rainfallInput.focus();
    } else if (e.key === 'Enter' && document.activeElement === rainfallInput) {
        form.dispatchEvent(new Event('submit'));
    }
});

/**
 * Debounce function for input changes
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Live validation on input change
 */
const liveValidate = debounce(() => {
    const temp = parseFloat(temperatureInput.value);
    const rain = parseFloat(rainfallInput.value);

    if (!isNaN(temp) && !isNaN(rain) && temp >= -50 && temp <= 150 && rain >= 0 && rain <= 10) {
        // Valid input - could enable auto-predict if desired
    }
}, 500);

temperatureInput.addEventListener('input', liveValidate);
rainfallInput.addEventListener('input', liveValidate);
