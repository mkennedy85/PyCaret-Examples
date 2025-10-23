# Project Scripts

Utility scripts for automating common tasks in the PyCaret Examples project.

## Available Scripts

### `download_datasets.py`

Automatically downloads all 5 Kaggle datasets required for the tutorial notebooks.

**Usage:**
```bash
uv run scripts/download_datasets.py
```

**What it does:**
- Downloads 5 custom Kaggle datasets
- Organizes them into appropriate subdirectories
- Unzips files automatically
- Provides detailed progress and error reporting

**Datasets downloaded:**
1. **California Housing Prices** → `datasets/regression/`
2. **Customer Segmentation** → `datasets/clustering/`
3. **Credit Card Fraud** → `datasets/anomaly/`
4. **Groceries Dataset** → `datasets/association/`
5. **Hourly Energy Consumption** → `datasets/timeseries/`

**Requirements:**
- Kaggle API credentials in `~/.kaggle/kaggle.json`
- Get credentials from: https://www.kaggle.com/account
- Set permissions: `chmod 600 ~/.kaggle/kaggle.json`

**Output:**
```
🚀 PyCaret Datasets Downloader
============================================================

============================================================
📥 Regression: California Housing Prices
============================================================
Downloading california-housing-prices.zip to datasets/regression
✅ Downloaded to: datasets/regression

[... continues for all 5 datasets ...]

============================================================
📊 DOWNLOAD SUMMARY
============================================================
✅ Successful: 5/5

🎉 All datasets downloaded successfully!

Datasets location: datasets/

Next steps:
1. Open notebooks in Jupyter: uv run jupyter notebook
2. Modify each notebook to use the new datasets
3. Run all cells and save outputs
```

**Troubleshooting:**

If downloads fail:
1. Check `~/.kaggle/kaggle.json` exists
2. Verify permissions: `chmod 600 ~/.kaggle/kaggle.json`
3. Get new API token from https://www.kaggle.com/account
4. Ensure you're not trying to download competition data (use datasets only)

---

### `run_all_notebooks.py`

Execute all Jupyter notebooks from the command line without opening a browser.

**Usage:**
```bash
uv run scripts/run_all_notebooks.py
```

**What it does:**
- Executes all 5 notebooks sequentially
- Uses `jupyter nbconvert` to run cells
- Saves output in place (overwrites notebooks with executed versions)
- Provides detailed progress and error reporting
- Sets 1-hour timeout per notebook

**Notebooks executed:**
1. `regression.ipynb`
2. `clustering.ipynb`
3. `anomaly-detection.ipynb`
4. `association.ipynb`
5. `time-series-forecasting.ipynb`

**Output:**
```
🚀 PyCaret Notebooks Batch Executor
======================================================================

======================================================================
📓 Executing: regression.ipynb
======================================================================
Started at: 2025-01-21 14:30:00
✅ SUCCESS: regression.ipynb
Completed at: 2025-01-21 14:42:15

[... continues for all notebooks ...]

======================================================================
📊 EXECUTION SUMMARY
======================================================================
✅ regression.ipynb: SUCCESS
✅ clustering.ipynb: SUCCESS
✅ anomaly-detection.ipynb: SUCCESS
✅ association.ipynb: SUCCESS
✅ time-series-forecasting.ipynb: SUCCESS

======================================================================
✅ Successful: 5/5
❌ Failed: 0/5
⚠️  Skipped: 0/5
⏱️  Total time: 1:23:45
======================================================================

🎉 All notebooks executed successfully!
```

**When to use:**
- Executing all notebooks automatically
- CI/CD pipelines
- Generating outputs without manual interaction
- Testing notebooks work end-to-end

---

### `run_notebooks_papermill.py`

Execute notebooks using Papermill (better progress reporting).

**Usage:**
```bash
# Install papermill first (script will prompt if not installed)
uv add papermill

# Run all notebooks
uv run scripts/run_notebooks_papermill.py
```

**Advantages over nbconvert:**
- Better progress bars
- Parameterization support (pass variables to notebooks)
- Better error messages
- Cell-by-cell execution tracking

**Usage is identical to `run_all_notebooks.py`**

---

### Manual Notebook Execution (Alternative)

If you prefer to run notebooks individually:

**Using nbconvert:**
```bash
# Execute single notebook in place
uv run jupyter nbconvert --to notebook --execute --inplace notebooks/regression.ipynb

# Execute and save to new file
uv run jupyter nbconvert --to notebook --execute notebooks/regression.ipynb --output regression_executed.ipynb
```

**Using papermill:**
```bash
# Install papermill
uv add papermill

# Execute notebook
uv run papermill notebooks/regression.ipynb notebooks/regression_output.ipynb

# Execute in place (overwrite)
uv run papermill notebooks/regression.ipynb notebooks/regression.ipynb
```

---

## Adding New Scripts

To add a new script:

1. Create `scripts/your_script.py`
2. Add docstring and command line usage
3. Run with: `uv run scripts/your_script.py`
4. Document in this README

**Example template:**
```python
"""
Brief description of what the script does.

Run with: uv run scripts/your_script.py
"""

def main():
    """Main script logic."""
    print("Hello from script!")

if __name__ == "__main__":
    main()
```
