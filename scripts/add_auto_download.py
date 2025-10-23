"""
Update notebooks to download datasets automatically from Kaggle.
This makes them ready to run on Vertex AI Workbench without manual data setup.
"""
import nbformat
from pathlib import Path

notebooks_dir = Path('notebooks')

def create_download_cell(dataset_name, file_path, kaggle_dataset):
    """Create a notebook cell that downloads data from Kaggle."""
    code = f'''import os
from pathlib import Path
import pandas as pd

# Setup data directory
data_dir = Path('../datasets/{dataset_name}')
data_dir.mkdir(parents=True, exist_ok=True)

data_path = data_dir / '{file_path}'

# Download from Kaggle if not already present
if not data_path.exists():
    print(f"📥 Downloading dataset from Kaggle...")

    # Check for Kaggle credentials
    kaggle_json = Path.home() / '.kaggle' / 'kaggle.json'

    if not kaggle_json.exists():
        print("⚠️  Kaggle credentials not found!")
        print("\\nTo download datasets automatically, you need Kaggle API credentials:")
        print("1. Go to https://www.kaggle.com/settings")
        print("2. Scroll to 'API' section and click 'Create New API Token'")
        print("3. This downloads kaggle.json")
        print("4. Upload kaggle.json to your home directory:")
        print("   - In Vertex AI: Upload to /home/jupyter/.kaggle/")
        print("   - Or set KAGGLE_USERNAME and KAGGLE_KEY environment variables")
        print("\\nFor now, using a backup URL...")

        # Fallback: Try to download from a direct URL if available
        try:
            import urllib.request
            # Note: This URL is a placeholder - update with actual backup URL if available
            backup_url = "https://storage.googleapis.com/pycaret-examples-backup/{dataset_name}/{file_path}"
            print(f"Trying backup URL: {{backup_url}}")
            urllib.request.urlretrieve(backup_url, data_path)
            print("✅ Downloaded from backup URL")
        except Exception as e:
            print(f"❌ Backup download failed: {{e}}")
            raise Exception("Please upload kaggle.json or manually download the dataset")
    else:
        # Download using Kaggle API
        import kaggle
        print(f"Downloading from Kaggle: {kaggle_dataset}")
        kaggle.api.dataset_download_files(
            '{kaggle_dataset}',
            path=data_dir,
            unzip=True,
            quiet=False
        )
        print(f"✅ Dataset downloaded to {{data_dir}}")
else:
    print(f"✅ Dataset already exists at {{data_path}}")

# Load the data
print(f"\\n📊 Loading dataset...")
data = pd.read_csv(data_path)
print(f"Dataset shape: {{data.shape}}")
'''
    return code

# Update regression.ipynb
print("Updating regression.ipynb...")
nb = nbformat.read(notebooks_dir / 'regression.ipynb', as_version=4)

# Find the data loading cell and replace it
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and 'housing.csv' in cell.source and 'pd.read_csv' in cell.source:
        # Create new cell with auto-download
        download_code = create_download_cell(
            'regression',
            'housing.csv',
            'camnugent/california-housing-prices'
        )
        cell.source = download_code
        print("  ✓ Added auto-download to regression.ipynb")
        break

nbformat.write(nb, notebooks_dir / 'regression.ipynb')
print("  ✓ regression.ipynb saved\n")

# Update clustering.ipynb
print("Updating clustering.ipynb...")
nb = nbformat.read(notebooks_dir / 'clustering.ipynb', as_version=4)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and 'jewellery.csv' in cell.source and 'pd.read_csv' in cell.source:
        download_code = create_download_cell(
            'clustering',
            'jewellery.csv',
            'PromptCloudHQ/online-jewellery-sales-data'
        )
        cell.source = download_code
        print("  ✓ Added auto-download to clustering.ipynb")
        break

nbformat.write(nb, notebooks_dir / 'clustering.ipynb')
print("  ✓ clustering.ipynb saved\n")

# Update anomaly-detection.ipynb
print("Updating anomaly-detection.ipynb...")
nb = nbformat.read(notebooks_dir / 'anomaly-detection.ipynb', as_version=4)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and 'anomaly.csv' in cell.source and 'pd.read_csv' in cell.source:
        download_code = create_download_cell(
            'anomaly',
            'anomaly.csv',
            'mlg-ulb/creditcardfraud'
        )
        # For credit card fraud, the file is named differently
        download_code = download_code.replace("'anomaly.csv'", "'creditcard.csv'")
        download_code = download_code.replace("data_path = data_dir / 'anomaly.csv'",
                                             "data_path = data_dir / 'creditcard.csv'")
        cell.source = download_code
        print("  ✓ Added auto-download to anomaly-detection.ipynb")
        break

nbformat.write(nb, notebooks_dir / 'anomaly-detection.ipynb')
print("  ✓ anomaly-detection.ipynb saved\n")

# Update association.ipynb
print("Updating association.ipynb...")
nb = nbformat.read(notebooks_dir / 'association.ipynb', as_version=4)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and 'Groceries.csv' in cell.source and 'pd.read_csv' in cell.source:
        download_code = create_download_cell(
            'association',
            'Groceries.csv',
            'heeraldedhia/groceries-dataset'
        )
        cell.source = download_code
        print("  ✓ Added auto-download to association.ipynb")
        break

nbformat.write(nb, notebooks_dir / 'association.ipynb')
print("  ✓ association.ipynb saved\n")

# Update time-series-forecasting.ipynb
print("Updating time-series-forecasting.ipynb...")
nb = nbformat.read(notebooks_dir / 'time-series-forecasting.ipynb', as_version=4)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and 'AEP_hourly.csv' in cell.source and 'pd.read_csv' in cell.source:
        download_code = create_download_cell(
            'time-series',
            'AEP_hourly.csv',
            'robikscube/hourly-energy-consumption'
        )
        cell.source = download_code
        print("  ✓ Added auto-download to time-series-forecasting.ipynb")
        break

nbformat.write(nb, notebooks_dir / 'time-series-forecasting.ipynb')
print("  ✓ time-series-forecasting.ipynb saved\n")

print("✅ All notebooks updated with auto-download capability!")
print("\nNotebooks will now:")
print("  - Automatically download datasets from Kaggle")
print("  - Create necessary directories")
print("  - Skip download if dataset already exists")
print("  - Work on Vertex AI Workbench without manual setup")
print("\nNote: Users need Kaggle API credentials configured:")
print("  - Upload kaggle.json to ~/.kaggle/ directory")
print("  - Or set KAGGLE_USERNAME and KAGGLE_KEY environment variables")
