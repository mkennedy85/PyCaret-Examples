#!/usr/bin/env bash
# Run specific notebooks with papermill
# Usage: ./run_specific_notebooks.sh notebook1.ipynb notebook2.ipynb

set -euo pipefail

cd "$(dirname "$0")"

# Check if notebooks provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <notebook1.ipynb> [notebook2.ipynb] ..."
    echo ""
    echo "Example:"
    echo "  $0 notebooks/03_anomaly-detection.ipynb notebooks/05_time-series-forecasting.ipynb"
    exit 1
fi

# Setup directories
mkdir -p outputs/executed_notebooks
mkdir -p logs

echo "=========================================="
echo "Running Specific Notebooks"
echo "=========================================="
echo ""

# Activate conda environment if available
if [ -f /opt/conda/etc/profile.d/conda.sh ]; then
    source /opt/conda/etc/profile.d/conda.sh
    conda activate pycaret310 2>/dev/null || echo "⚠️  pycaret310 env not found, using base"
fi

# Track start time
START_TIME=$(date +%s)

# Process each notebook
TOTAL=$#
CURRENT=0
SUCCESS=0
FAILED=0

for notebook in "$@"; do
    CURRENT=$((CURRENT + 1))

    # Get notebook name without path
    notebook_name=$(basename "$notebook")
    notebook_base="${notebook_name%.ipynb}"

    echo "[$CURRENT/$TOTAL] Processing: $notebook_name"
    echo "Started at: $(date '+%Y-%m-%d %H:%M:%S')"

    output_path="outputs/executed_notebooks/${notebook_name}"
    log_path="logs/${notebook_base}_$(date +%Y%m%d_%H%M%S).log"

    # Run papermill
    if papermill "$notebook" "$output_path" > "$log_path" 2>&1; then
        echo "  ✅ Success"
        SUCCESS=$((SUCCESS + 1))
    else
        echo "  ❌ Failed - check log: $log_path"
        FAILED=$((FAILED + 1))
    fi

    echo ""
done

# Calculate duration
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))
MINUTES=$((DURATION / 60))
SECONDS=$((DURATION % 60))

echo "=========================================="
echo "Execution Complete"
echo "=========================================="
echo "Total notebooks: $TOTAL"
echo "Succeeded: $SUCCESS"
echo "Failed: $FAILED"
echo "Duration: ${MINUTES}m ${SECONDS}s"
echo ""
echo "Output notebooks: outputs/executed_notebooks/"
echo "Logs: logs/"
