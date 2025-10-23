"""
Execute all PyCaret notebooks from the command line.

This script runs all 5 notebooks sequentially, saving the output in place.
Run with: uv run scripts/run_all_notebooks.py
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime


def run_notebook(notebook_path: Path, timeout: int = 3600, allow_errors: bool = False) -> bool:
    """
    Execute a Jupyter notebook using nbconvert.

    Args:
        notebook_path: Path to the notebook file
        timeout: Maximum execution time in seconds (default: 1 hour)
        allow_errors: If True, continue executing even if cells fail (default: False)

    Returns:
        True if successful, False otherwise
    """
    print(f"\n{'='*70}")
    print(f"📓 Executing: {notebook_path.name}")
    print(f"{'='*70}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        # Execute notebook in place
        cmd = [
            "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.timeout={}".format(timeout),
            str(notebook_path)
        ]

        # Add allow_errors if specified
        if allow_errors:
            cmd.append("--ExecutePreprocessor.allow_errors=True")

        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )

        print(f"✅ SUCCESS: {notebook_path.name}")
        print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ FAILED: {notebook_path.name}")
        print(f"Error: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ ERROR: {notebook_path.name}")
        print(f"Error: {str(e)}")
        return False


def main():
    """Execute all notebooks in sequence."""
    print("🚀 PyCaret Notebooks Batch Executor")
    print("="*70)

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

        success = run_notebook(notebook_path, timeout=1800)  # 30 min timeout (reduced for faster testing)
        results[notebook_name] = "SUCCESS" if success else "FAILED"

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
