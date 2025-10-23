# PyCaret Tutorials - 5 End-to-End ML Notebooks

Five comprehensive PyCaret machine learning notebooks demonstrating AutoML capabilities.

**Course:** CMPE-255 Data Mining | **Institution:** San José State University

---

## 📚 The 5 Notebooks

| Notebook | ML Task | What You'll Learn |
|----------|---------|-------------------|
| **regression.ipynb** | Supervised Learning | AutoML with 25+ models, hyperparameter tuning, ensembling, SHAP interpretation |
| **clustering.ipynb** | Unsupervised Learning | K-Means, DBSCAN, elbow method, customer segmentation |
| **anomaly-detection.ipynb** | Anomaly Detection | Isolation Forest, outlier detection, fraud detection |
| **association.ipynb** | Association Rules | Market basket analysis, Apriori algorithm, product recommendations |
| **time-series-forecasting.ipynb** | Time Series | ARIMA, Prophet, seasonal decomposition, forecasting |

---

## 🚀 Quick Start

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Configure Kaggle API (for auto-download)
# Get API token from https://www.kaggle.com/settings
mkdir -p ~/.kaggle
mv kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Start Jupyter
uv run jupyter notebook
```

Open any notebook and run all cells - datasets download automatically!

---

## ✨ Key Features

✅ **Auto-Download** - Datasets fetch automatically from Kaggle (no manual setup)
✅ **Optimized** - Uses `fold=3` for 60-70% faster execution
✅ **Comprehensive** - Covers 5 major ML paradigms
✅ **Production-Ready** - Includes model deployment examples

---

## 📖 What Each Notebook Demonstrates

### 1. regression.ipynb
**Dataset:** California Housing Prices (20,640 samples)

- ✅ AutoML: Compare 25+ regression models automatically
- ✅ Hyperparameter tuning with RandomSearch and Optuna
- ✅ Ensemble methods: bagging, boosting, stacking, blending
- ✅ SHAP values for model interpretation
- ✅ Model persistence and deployment

**Key Code:**
```python
from pycaret.regression import *
setup(data, target='median_house_value', fold=3, session_id=123)
best = compare_models(include=['lr', 'ridge', 'rf', 'lightgbm', 'gbr'])
tuned = tune_model(best)
save_model(best, 'model')
```

### 2. clustering.ipynb
**Dataset:** Jewellery Customer Data

- ✅ K-Means, DBSCAN, hierarchical clustering
- ✅ Elbow method for optimal clusters
- ✅ Silhouette analysis
- ✅ Customer segmentation strategies
- ✅ Cluster visualization

**Key Code:**
```python
from pycaret.clustering import *
setup(data, fold=3, session_id=123)
kmeans = create_model('kmeans')
plot_model(kmeans, plot='elbow')
results = assign_model(kmeans)
```

### 3. anomaly-detection.ipynb
**Dataset:** Credit Card Fraud (284,807 transactions)

- ✅ Isolation Forest algorithm
- ✅ KNN-based outlier detection
- ✅ Contamination parameter tuning
- ✅ Anomaly scoring and ranking
- ✅ Fraud detection pipeline

**Key Code:**
```python
from pycaret.anomaly import *
setup(data, session_id=42, normalize=True)
iforest = create_model('iforest')
results = assign_model(iforest)
```

### 4. association.ipynb
**Dataset:** Groceries Market Basket

- ✅ Market basket analysis
- ✅ Apriori algorithm
- ✅ Support, confidence, lift metrics
- ✅ Product recommendation rules
- ✅ 2D and 3D rule visualization

**Key Code:**
```python
import mlxtend
from mlxtend.frequent_patterns import apriori, association_rules
frequent_itemsets = apriori(basket, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
```

### 5. time-series-forecasting.ipynb
**Dataset:** Hourly Energy Consumption

- ✅ ARIMA, Prophet, exponential smoothing
- ✅ Seasonal decomposition
- ✅ Forecast horizons
- ✅ Cross-validation for time series
- ✅ Forecast evaluation metrics

**Key Code:**
```python
from pycaret.time_series import *
setup(data, target='value', fh=24, fold=3, session_id=42)
best = compare_models(n_select=1)
forecast = predict_model(best)
```

---

## 🔧 Technical Details

### Dependencies
- **Python:** 3.10 or 3.11 (3.12 not supported yet)
- **PyCaret:** 3.3.2
- **Key Libraries:** scikit-learn, xgboost, lightgbm, statsmodels, mlxtend

All managed automatically by `uv`.

### Datasets
All datasets download automatically from Kaggle when you run the notebooks:

| Dataset | Size | Source |
|---------|------|--------|
| California Housing | ~600 KB | [Kaggle](https://www.kaggle.com/camnugent/california-housing-prices) |
| Jewellery Sales | ~2 MB | [Kaggle](https://www.kaggle.com/PromptCloudHQ/online-jewellery-sales-data) |
| Credit Card Fraud | ~150 MB | [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud) |
| Groceries | ~300 KB | [Kaggle](https://www.kaggle.com/heeraldedhia/groceries-dataset) |
| Energy Consumption | ~2 MB | [Kaggle](https://www.kaggle.com/robikscube/hourly-energy-consumption) |

**Total:** ~155 MB

### Performance Optimizations
- `fold=3` instead of default 10 (70% faster cross-validation)
- Limited model comparison in regression (5 models vs 25+)
- Reduced forecast horizon in time series
- **Result:** ~15 minutes total execution time (vs ~28 minutes unoptimized)

---

## 📁 Project Structure

```
Pycaret-Examples/
├── notebooks/                    # 5 PyCaret notebooks
│   ├── regression.ipynb
│   ├── clustering.ipynb
│   ├── anomaly-detection.ipynb
│   ├── association.ipynb
│   └── time-series-forecasting.ipynb
├── pyproject.toml               # Python dependencies (uv)
├── .python-version              # Python 3.11
└── README.md                    # This file
```

---

## 🎯 Common Commands

```bash
# Setup
uv sync

# Run Jupyter
uv run jupyter notebook
```

Open any notebook in the `notebooks/` folder and run all cells!

---

## 💡 Tips

1. **Start with regression.ipynb** - Most comprehensive tutorial
2. **Read the comments** - Each notebook is heavily documented
3. **Experiment** - Try different parameters and models
4. **Check the outputs** - PyCaret creates beautiful visualizations
5. **Set up Kaggle credentials** once: `~/.kaggle/kaggle.json` for auto-download

---

## 📚 Resources

- **PyCaret Docs:** https://pycaret.readthedocs.io
- **PyCaret GitHub:** https://github.com/pycaret/pycaret
- **uv Package Manager:** https://github.com/astral-sh/uv
- **Kaggle API:** https://github.com/Kaggle/kaggle-api

---

## 🎓 About

**Course:** CMPE-255 Data Mining
**Institution:** San José State University
**Platform:** Python 3.11, PyCaret 3.3.2

These notebooks demonstrate modern AutoML workflows using PyCaret's low-code approach, covering the full spectrum of machine learning tasks from supervised learning to time series forecasting.

---

**Ready to explore PyCaret?** Start with `uv sync` and `uv run jupyter notebook`! 🚀
