"""
Quick test script - runs notebooks with shorter timeout for fast validation.

This is a simplified test that just runs the notebooks with:
- Shorter timeout (10 min per notebook)
- Allows errors (to see all failures at once)

For speed improvements, manually edit notebooks to:
1. Add fold=3 to setup() calls
2. Limit compare_models() to fewer models

Run with: uv run scripts/quick_test.py
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime


def run_notebook(notebook_path: Path, timeout: int = 600, allow_errors: bool = False) -> bool:
    """Execute notebook with short timeout."""
    print(f"\n{'='*70}")
    print(f"🚀 Testing: {notebook_path.name}")
    print(f"{'='*70}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        cmd = [
            "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--ExecutePreprocessor.timeout={}".format(timeout),
            str(notebook_path),
            "--output", str(notebook_path),  # Overwrite in place
        ]

        if allow_errors:
            cmd.append("--ExecutePreprocessor.allow_errors=True")

        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ SUCCESS")
        print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ FAILED")
        # Only show last 500 chars of error to keep it readable
        error_msg = e.stderr[-500:] if len(e.stderr) > 500 else e.stderr
        print(f"Error: ...{error_msg}")
        return False
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False


def main():
    """Quick test all notebooks."""
    print("⚡ PyCaret Quick Test Runner")
    print("="*70)
    print("Testing with:")
    print("  - 10 min timeout per notebook (vs 30 min in full suite)")
    print("  - Sequential execution")
    print()
    print("💡 TIP: To speed up notebooks further, manually edit them to:")
    print("   1. Add 'fold=3' parameter to setup() calls")
    print("   2. Use compare_models(n_select=1) to test fewer models")
    print("="*70)

    project_root = Path(__file__).parent.parent
    notebooks_dir = project_root / "notebooks"

    notebooks = [
        "regression.ipynb",
        "clustering.ipynb",
        "anomaly-detection.ipynb",
        "association.ipynb",
        "time-series-forecasting.ipynb"
    ]

    results = {}
    start_time = datetime.now()

    for notebook_name in notebooks:
        notebook_path = notebooks_dir / notebook_name

        if not notebook_path.exists():
            print(f"⚠️  SKIP: {notebook_name} (not found)")
            results[notebook_name] = "SKIPPED"
            continue

        # Run with short timeout
        success = run_notebook(notebook_path, timeout=600, allow_errors=False)
        results[notebook_name] = "SUCCESS" if success else "FAILED"

    # Print summary
    end_time = datetime.now()
    duration = end_time - start_time

    print(f"\n{'='*70}")
    print("📊 QUICK TEST SUMMARY")
    print(f"{'='*70}")

    success_count = sum(1 for s in results.values() if s == "SUCCESS")
    failed_count = sum(1 for s in results.values() if s == "FAILED")

    for notebook, status in results.items():
        emoji = "✅" if status == "SUCCESS" else "❌" if status == "FAILED" else "⚠️"
        print(f"{emoji} {notebook}: {status}")

    print(f"\n{'='*70}")
    print(f"✅ Passed: {success_count}/{len(notebooks)}")
    print(f"❌ Failed: {failed_count}/{len(notebooks)}")
    print(f"⏱️  Total time: {duration}")
    print(f"{'='*70}")

    if failed_count > 0:
        print("\n⚠️  Some tests failed.")
        print("💡 These failures may be due to timeout (10 min limit).")
        print("   Run 'uv run scripts/run_all_notebooks.py' for full validation (30 min timeout).")
        sys.exit(1)
    else:
        print("\n🎉 All quick tests passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
