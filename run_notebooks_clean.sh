#\!/usr/bin/env bash
set -euo pipefail

# =============================================================================
# PyCaret Notebooks Runner - Clean Logging Version
# =============================================================================
# This script executes all 5 PyCaret tutorial notebooks sequentially using
# papermill, with cleaner logging that filters out JSON/metadata.
# =============================================================================

# --- Configuration ---
KERNEL_NAME="${KERNEL_NAME:-pycaret-py310}"
ENV_NAME="${ENV_NAME:-pycaret310}"
NON_INTERACTIVE="${NON_INTERACTIVE:-1}"

NB_DIR="notebooks"
OUT_DIR="outputs/executed_notebooks"
LOG_DIR="logs"
TS="$(date +%Y%m%d-%H%M%S)"

# List of notebooks in execution order
NOTEBOOKS=(
  "01_regression.ipynb"
  "02_clustering.ipynb"
  "03_anomaly-detection.ipynb"
  "04_association.ipynb"
  "05_time-series-forecasting.ipynb"
)

# Optional parameters to pass into notebooks
PM_PARAMS=(
  -p run_id "$TS"
  -p auto_download "true"
)

# --- Setup ---
mkdir -p "$OUT_DIR" "$LOG_DIR"

# Activate conda non-interactively
if [ -f "/opt/conda/etc/profile.d/conda.sh" ]; then
    source /opt/conda/etc/profile.d/conda.sh
    conda activate "$ENV_NAME" 2>/dev/null || true
fi

# Ensure papermill is present
python -m pip show papermill >/dev/null 2>&1 || python -m pip install -q papermill nbformat

# Check if papermill is installed
if \! command -v papermill &> /dev/null; then
    echo "❌ Error: papermill is not installed"
    echo "Install it with: pip install papermill"
    exit 1
fi

# Kaggle creds check
if [ \! -f "$HOME/.kaggle/kaggle.json" ]; then
  echo "⚠️  ~/.kaggle/kaggle.json missing."
  if [ "$NON_INTERACTIVE" \!= "1" ]; then
    read -p "Continue anyway? [y/N] " -n 1 -r; echo
    [[ $REPLY =~ ^[Yy]$ ]] || exit 1
  fi
fi

# --- Execute Notebooks Sequentially ---
TOTAL=${#NOTEBOOKS[@]}
CURRENT=0
FAILED=()
SUCCEEDED=()

echo ""
echo "=========================================="
echo "Starting Notebook Execution"
echo "=========================================="
echo "Time: $(date)"
echo "Kernel: $KERNEL_NAME"
echo "Notebooks: $TOTAL"
echo ""

for NB in "${NOTEBOOKS[@]}"; do
  CURRENT=$((CURRENT + 1))
  in="$NB_DIR/$NB"
  out="$OUT_DIR/${NB%.ipynb}_executed_${TS}.ipynb"
  log="$LOG_DIR/${NB%.ipynb}_${TS}.log"

  echo ""
  echo "=========================================="
  echo "[$CURRENT/$TOTAL] Running: $NB"
  echo "=========================================="
  echo "Input:  $in"
  echo "Output: $out"
  echo "Log:    $log"
  echo ""

  # Execute with papermill and capture output
  # Use --log-output to get cleaner progress messages
  if papermill "$in" "$out" \
       -k "$KERNEL_NAME" \
       "${PM_PARAMS[@]}" \
       --log-output \
       --progress-bar \
       > "$log" 2>&1; then
    echo ""
    echo "✅ Completed: $NB"
    SUCCEEDED+=("$NB")
    
    # Show last few lines of log (summary)
    echo ""
    echo "Last 5 lines of output:"
    tail -5 "$log" || true
  else
    echo ""
    echo "❌ Failed: $NB"
    FAILED+=("$NB")

    # Show error from log
    echo ""
    echo "Error (last 20 lines):"
    tail -20 "$log" || true

    # Handle failure
    if [ "$NON_INTERACTIVE" = "1" ]; then
      echo "Continuing with remaining notebooks (NON_INTERACTIVE=1)."
      continue
    else
      echo ""
      read -p "Continue with remaining notebooks? [y/N] " -n 1 -r
      echo
      if [[ \! $REPLY =~ ^[Yy]$ ]]; then
        echo "Execution halted at user request."
        break
      fi
    fi
  fi
done

# --- Summary ---
echo ""
echo "=========================================="
echo "Execution Summary"
echo "=========================================="
echo "End time: $(date)"
echo "Run ID: $TS"
echo ""
echo "Succeeded: ${#SUCCEEDED[@]}/$TOTAL"
for nb in "${SUCCEEDED[@]}"; do
  echo "  ✅ $nb"
done

if [ ${#FAILED[@]} -gt 0 ]; then
  echo ""
  echo "Failed: ${#FAILED[@]}/$TOTAL"
  for nb in "${FAILED[@]}"; do
    echo "  ❌ $nb"
  done
  echo ""
  echo "Check logs in $LOG_DIR/ for error details"
  exit 1
fi

echo ""
echo "🎉 All notebooks completed successfully\!"
echo ""
echo "Outputs saved to: $OUT_DIR"
echo "Logs saved to: $LOG_DIR"
echo "=========================================="
