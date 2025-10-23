"""
Execute all PyCaret notebooks using Papermill.

Papermill is specifically designed for notebook execution and provides better
error handling and progress reporting than nbconvert.

Run with: uv run scripts/run_notebooks_papermill.py
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime


def check_papermill_installed() -> bool:
    """Check if papermill is installed."""
    try:
        import papermill
        return True
    except ImportError:
        return False


def install_papermill():
    """Install papermill using uv."""
    print("📦 Installing papermill...")
    try:
        subprocess.run(["uv", "add", "papermill"], check=True)
        print("✅ Papermill installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install papermill")
        return False


def run_notebook_papermill(input_path: Path, output_path: Path = None) -> bool:
    """
    Execute a notebook using papermill.

    Args:
        input_path: Path to input notebook
        output_path: Path to output notebook (if None, overwrites input)

    Returns:
        True if successful, False otherwise
    """
    if output_path is None:
        output_path = input_path

    print(f"\n{'='*70}")
    print(f"📓 Executing: {input_path.name}")
    print(f"{'='*70}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        # Import papermill
        import papermill as pm

        # Execute notebook
        pm.execute_notebook(
            str(input_path),
            str(output_path),
            kernel_name='python3',
            progress_bar=True,
            request_save_on_cell_execute=True
        )

        print(f"✅ SUCCESS: {input_path.name}")
        print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True

    except Exception as e:
        print(f"❌ FAILED: {input_path.name}")
        print(f"Error: {str(e)}")
        return False


def main():
    """Execute all notebooks using papermill."""
    print("🚀 PyCaret Notebooks Executor (Papermill)")
    print("="*70)

    # Check if papermill is installed
    if not check_papermill_installed():
        print("⚠️  Papermill not found")
        if not install_papermill():
            print("\n❌ Cannot proceed without papermill")
            print("Please install manually: uv add papermill")
            sys.exit(1)

    # Get project root
    project_root = Path(__file__).parent.parent
    notebooks_dir = project_root / "notebooks"

    # Define notebooks in execution order
    notebooks = [
        "regression.ipynb",
        "clustering.ipynb",
        "anomaly-detection.ipynb",
        "association.ipynb",
        "time-series-forecasting.ipynb"
    ]

    # Track results
    results = {}
    start_time = datetime.now()

    # Execute each notebook
    for notebook_name in notebooks:
        notebook_path = notebooks_dir / notebook_name

        if not notebook_path.exists():
            print(f"⚠️  SKIP: {notebook_name} (not found)")
            results[notebook_name] = "SKIPPED"
            continue

        success = run_notebook_papermill(notebook_path)
        results[notebook_name] = "SUCCESS" if success else "FAILED"

        # Stop on first failure (optional - comment out to continue)
        # if not success:
        #     print(f"\n⚠️  Stopping execution due to failure in {notebook_name}")
        #     break

    # Print summary
    end_time = datetime.now()
    duration = end_time - start_time

    print(f"\n{'='*70}")
    print("📊 EXECUTION SUMMARY")
    print(f"{'='*70}")

    success_count = sum(1 for status in results.values() if status == "SUCCESS")
    failed_count = sum(1 for status in results.values() if status == "FAILED")
    skipped_count = sum(1 for status in results.values() if status == "SKIPPED")

    for notebook, status in results.items():
        emoji = "✅" if status == "SUCCESS" else "❌" if status == "FAILED" else "⚠️"
        print(f"{emoji} {notebook}: {status}")

    print(f"\n{'='*70}")
    print(f"✅ Successful: {success_count}/{len(notebooks)}")
    print(f"❌ Failed: {failed_count}/{len(notebooks)}")
    print(f"⚠️  Skipped: {skipped_count}/{len(notebooks)}")
    print(f"⏱️  Total time: {duration}")
    print(f"{'='*70}")

    # Exit with error if any failed
    if failed_count > 0:
        print("\n⚠️  Some notebooks failed. Check the output above for details.")
        sys.exit(1)
    else:
        print("\n🎉 All notebooks executed successfully!")
        print("\nNext steps:")
        print("1. Review notebooks to see all outputs")
        print("2. Check outputs/ directory for saved models")
        print("3. Record your video tutorials")
        sys.exit(0)


if __name__ == "__main__":
    main()
