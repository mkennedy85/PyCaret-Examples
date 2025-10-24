# PyCaret Tutorials - 5 End-to-End ML Notebooks

> **✨ 5 Complete PyCaret Examples**
> Fully executed notebooks with outputs demonstrating AutoML across 5 machine learning paradigms.
> See [executed notebooks](./executed_notebooks/) for complete results with visualizations.

Five comprehensive PyCaret machine learning notebooks demonstrating AutoML capabilities across regression, clustering, anomaly detection, association rules, and time series forecasting.

**Course:** CMPE-255 Data Mining | **Institution:** San José State University

---

## 📊 Available Examples

| Example | ML Paradigm | Status | Highlights |
|---------|-------------|--------|------------|
| **01_regression** | Supervised Learning | ✅ With outputs | AutoML comparison, model tuning, deployment |
| **02_clustering** | Unsupervised Learning | ✅ With outputs | Customer segmentation, elbow method, 3D plots |
| **03_anomaly-detection** | Outlier Detection | ✅ With outputs | Fraud detection, 3 algorithms, evaluation |
| **04_association** | Market Basket | ✅ With outputs | Apriori rules, lift analysis, visualizations |
| **05_time-series-forecasting** | Time Series | ✅ With outputs | Energy forecasting, model comparison |

**📁 View Results:** All executed notebooks with full outputs and visualizations are in [`executed_notebooks/`](./executed_notebooks/)

---

## 📚 The 5 Notebooks

| Notebook | ML Task | What You'll Learn |
|----------|---------|-------------------|
| **01_regression.ipynb** | Supervised Learning | AutoML with 25+ models, hyperparameter tuning, ensembling, SHAP interpretation |
| **02_clustering.ipynb** | Unsupervised Learning | K-Means, DBSCAN, elbow method, customer segmentation |
| **03_anomaly-detection.ipynb** | Anomaly Detection | Isolation Forest, outlier detection, fraud detection |
| **04_association.ipynb** | Association Rules | Market basket analysis, Apriori algorithm, product recommendations |
| **05_time-series-forecasting.ipynb** | Time Series | ARIMA, Prophet, seasonal decomposition, forecasting |

---

## 🚀 Quick Start

### Local Development

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

### Vertex AI Workbench

```bash
# Clone or upload this repository to your Workbench instance

# Install dependencies using pip
pip install -e .

# Configure Kaggle API (for auto-download)
# Get API token from https://www.kaggle.com/settings
# Upload kaggle.json to Workbench, then:
mkdir -p ~/.kaggle
mv kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Launch Jupyter (already installed in Workbench)
jupyter notebook
```

Open any notebook and run all cells - datasets download automatically!

---

## ✨ Key Features

✅ **Auto-Download** - Datasets fetch automatically from Kaggle (no manual setup)
✅ **Optimized** - Uses `fold=3` for 60-70% faster execution
✅ **Comprehensive** - Covers 5 major ML paradigms
✅ **Production-Ready** - Includes model deployment examples
✅ **Cloud-Ready** - Works on Vertex AI Workbench or locally

---

## 🎥 Video Walkthroughs

Watch 1-minute overviews of each notebook:

### 1. Regression - California Housing Prices

https://github.com/mkennedy85/PyCaret-Examples/raw/main/videos/01_regression.mp4

### 2. Clustering - Customer Segmentation

https://github.com/mkennedy85/PyCaret-Examples/raw/main/videos/02_clustering.mp4

### 3. Anomaly Detection - Credit Card Fraud

https://github.com/mkennedy85/PyCaret-Examples/raw/main/videos/03_anomaly_detection.mp4

### 4. Association Rules - Market Basket Analysis

https://github.com/mkennedy85/PyCaret-Examples/raw/main/videos/04_association.mp4

### 5. Time Series - Energy Forecasting

https://github.com/mkennedy85/PyCaret-Examples/raw/main/videos/05_time_forecasting.mp4

---

## 📖 What Each Notebook Demonstrates

### 1. 01_regression.ipynb
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

### 2. 02_clustering.ipynb
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

### 3. 03_anomaly-detection.ipynb
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

### 4. 04_association.ipynb
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

### 5. 05_time-series-forecasting.ipynb
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
│   ├── 01_regression.ipynb
│   ├── 02_clustering.ipynb
│   ├── 03_anomaly-detection.ipynb
│   ├── 04_association.ipynb
│   └── 05_time-series-forecasting.ipynb
├── run_notebooks.sh             # Batch execution script (papermill)
├── pyproject.toml               # Python dependencies (uv)
├── .python-version              # Python 3.10
└── README.md                    # This file
```

---

## 🎯 Common Commands

### Local Development
```bash
# Setup
uv sync

# Run Jupyter
uv run jupyter notebook

# Run all notebooks with papermill (batch execution)
./run_notebooks.sh
```

### Vertex AI Workbench
```bash
# Setup (one-time)
pip install -e .
pip install papermill  # For batch execution

# Run Jupyter
jupyter notebook

# Run all notebooks with papermill (batch execution)
./run_notebooks.sh
```

Open any notebook in the `notebooks/` folder and run all cells!

---

## 🔄 Batch Execution with Papermill

You can execute all 5 notebooks sequentially using the included `run_notebooks.sh` script:

```bash
# Install papermill first
pip install papermill  # or: uv pip install papermill

# Run all notebooks
./run_notebooks.sh
```

**What the script does:**
- Executes notebooks in order: 01 → 02 → 03 → 04 → 05
- Saves executed notebooks to `outputs/executed_notebooks/`
- Creates detailed logs in `logs/`
- Checks for Kaggle credentials before starting
- Allows continuing on errors (prompts user)
- Provides detailed progress and summary

**Customization:**
```bash
# Use a specific kernel (default is pycaret310)
KERNEL_NAME="my-kernel" ./run_notebooks.sh

# Or edit the script to change:
# - Output directories
# - Notebook order
# - Parameters passed to notebooks
```

**Output structure:**
```
outputs/executed_notebooks/
├── 01_regression_executed_20251022-184530.ipynb
├── 02_clustering_executed_20251022-184530.ipynb
├── ...

logs/
├── 01_regression_20251022-184530.log
├── 02_clustering_20251022-184530.log
├── ...
```

---

## 💡 Tips

### For Local Development
1. **Use uv** for fast dependency installation (10-100x faster than pip)
2. **Start with 01_regression.ipynb** - Most comprehensive tutorial
3. **Set up Kaggle credentials** once: `~/.kaggle/kaggle.json` for auto-download
4. **Use run_notebooks.sh** for automated batch execution of all 5 notebooks

### For Vertex AI Workbench
1. **Use pip install -e .** - Installs from pyproject.toml automatically
2. **Upload kaggle.json** to enable auto-download of datasets
3. **Stop your instance** when not in use to avoid charges

### For All Users
1. **Read the comments** - Each notebook is heavily documented
2. **Experiment** - Try different parameters and models
3. **Check the outputs** - PyCaret creates beautiful visualizations

---

## 📚 Resources

- **PyCaret Docs:** https://pycaret.readthedocs.io
- **PyCaret GitHub:** https://github.com/pycaret/pycaret
- **Vertex AI Workbench:** https://cloud.google.com/vertex-ai/docs/workbench
- **uv Package Manager:** https://github.com/astral-sh/uv
- **Kaggle API:** https://github.com/Kaggle/kaggle-api

---

## 🎓 About

**Course:** CMPE-255 Data Mining
**Institution:** San José State University
**Platform:** Python 3.10/3.11, PyCaret 3.3.2

These notebooks demonstrate modern AutoML workflows using PyCaret's low-code approach, covering the full spectrum of machine learning tasks from supervised learning to time series forecasting.

---

**Ready to explore PyCaret?** Start with `uv sync` and `uv run jupyter notebook`! 🚀
