#!/usr/bin/env bash
# Run the 2 fixed notebooks in background
# Usage: ./run_fixed_notebooks_background.sh

set -euo pipefail

cd "$(dirname "$0")"

echo "=========================================="
echo "Running Fixed Notebooks in Background"
echo "=========================================="
echo ""
echo "This will run:"
echo "  - 03_anomaly-detection.ipynb"
echo "  - 05_time-series-forecasting.ipynb"
echo ""
echo "Starting in background..."

# Run in background with nohup
nohup bash -c '
    source /opt/conda/etc/profile.d/conda.sh 2>/dev/null || true
    conda activate pycaret310 2>/dev/null || true

    ./run_specific_notebooks.sh \
        notebooks/03_anomaly-detection.ipynb \
        notebooks/05_time-series-forecasting.ipynb

    rm -f run_fixed.pid
' > nohup_fixed.out 2>&1 &

# Save PID
echo $! > run_fixed.pid

echo "✅ Started in background!"
echo ""
echo "Process ID: $(cat run_fixed.pid)"
echo "Output log: nohup_fixed.out"
echo ""
echo "Monitor progress:"
echo "  tail -f nohup_fixed.out"
echo ""
echo "Check if running:"
echo "  ps -fp \$(cat run_fixed.pid)"
echo ""
echo "Stop execution:"
echo "  kill \$(cat run_fixed.pid)"
echo ""
echo "Expected completion: ~20-30 minutes"
echo "You can now close your browser!"
