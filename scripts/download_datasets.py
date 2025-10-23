"""
Download all datasets for PyCaret notebooks.

This script downloads Kaggle datasets for each of the 5 PyCaret tutorial notebooks.
Run with: uv run scripts/download_datasets.py
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str]) -> bool:
    """Run a command and return success status."""
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False


def download_dataset(dataset: str, output_dir: Path, description: str) -> bool:
    """Download and unzip a Kaggle dataset."""
    print(f"\n{'='*60}")
    print(f"📥 {description}")
    print(f"{'='*60}")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Download and unzip
    cmd = [
        "kaggle", "datasets", "download",
        "-d", dataset,
        "-p", str(output_dir),
        "--unzip"
    ]

    return run_command(cmd)


def main():
    """Download all datasets."""
    print("🚀 PyCaret Datasets Downloader")
    print("="*60)

    # Get project root (parent of scripts directory)
    project_root = Path(__file__).parent.parent
    datasets_dir = project_root / "datasets"

    # Define datasets for each notebook
    datasets = [
        {
            "name": "camnugent/california-housing-prices",
            "dir": datasets_dir / "regression",
            "desc": "Regression: California Housing Prices"
        },
        {
            "name": "vjchoudhary7/customer-segmentation-tutorial-in-python",
            "dir": datasets_dir / "clustering",
            "desc": "Clustering: Customer Segmentation"
        },
        {
            "name": "mlg-ulb/creditcardfraud",
            "dir": datasets_dir / "anomaly",
            "desc": "Anomaly Detection: Credit Card Fraud"
        },
        {
            "name": "heeraldedhia/groceries-dataset",
            "dir": datasets_dir / "association",
            "desc": "Association Rules: Groceries"
        },
        {
            "name": "robikscube/hourly-energy-consumption",
            "dir": datasets_dir / "timeseries",
            "desc": "Time Series: Hourly Energy Consumption"
        }
    ]

    # Download each dataset
    success_count = 0
    failed = []

    for dataset in datasets:
        if download_dataset(dataset["name"], dataset["dir"], dataset["desc"]):
            success_count += 1
            print(f"✅ Downloaded to: {dataset['dir']}")
        else:
            failed.append(dataset["desc"])
            print(f"❌ Failed to download")

    # Summary
    print(f"\n{'='*60}")
    print("📊 DOWNLOAD SUMMARY")
    print(f"{'='*60}")
    print(f"✅ Successful: {success_count}/{len(datasets)}")

    if failed:
        print(f"❌ Failed: {len(failed)}")
        for item in failed:
            print(f"   - {item}")
        print("\nTroubleshooting:")
        print("1. Check ~/.kaggle/kaggle.json exists")
        print("2. Verify permissions: chmod 600 ~/.kaggle/kaggle.json")
        print("3. Get new API token from https://www.kaggle.com/account")
        sys.exit(1)
    else:
        print("\n🎉 All datasets downloaded successfully!")
        print(f"\nDatasets location: {datasets_dir}")
        print("\nNext steps:")
        print("1. Open notebooks in Jupyter: uv run jupyter notebook")
        print("2. Modify each notebook to use the new datasets")
        print("3. Run all cells and save outputs")


if __name__ == "__main__":
    main()
