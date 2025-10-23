#!/usr/bin/env bash
# =============================================================================
# Run Notebooks in Background - Detached Mode
# =============================================================================
# This script starts notebook execution in the background using nohup,
# allowing you to close your browser/terminal safely.
#
# Usage:
#   ./run_notebooks_background.sh
#
# Monitor progress:
#   tail -f nohup.out
#   tail -f logs/progress.log
#
# Check status:
#   cat run.pid  # Get process ID
#   ps -fp $(cat run.pid)  # Check if still running
#
# Stop execution:
#   kill $(cat run.pid)
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if already running
if [ -f run.pid ]; then
    PID=$(cat run.pid)
    if ps -p "$PID" > /dev/null 2>&1; then
        echo "❌ Error: Notebooks are already running (PID: $PID)"
        echo ""
        echo "To monitor: tail -f nohup.out"
        echo "To stop: kill $PID"
        exit 1
    else
        # Stale PID file
        rm run.pid
    fi
fi

# Start in background with nohup
echo "🚀 Starting notebook execution in background..."
echo ""

# Use nohup to detach from terminal
nohup bash -c '
    # Source conda
    if [ -f /opt/conda/etc/profile.d/conda.sh ]; then
        source /opt/conda/etc/profile.d/conda.sh
        conda activate pycaret310 2>/dev/null || true
    fi

    # Run the notebooks
    ./run_notebooks.sh

    # Clean up PID file when done
    rm -f run.pid
' > nohup.out 2>&1 &

# Save PID
echo $! > run.pid

PID=$(cat run.pid)

echo "✅ Notebook execution started in background!"
echo ""
echo "Process ID: $PID"
echo "Status file: run.pid"
echo ""
echo "=========================================="
echo "Monitor Progress:"
echo "=========================================="
echo "  tail -f nohup.out              # Main output"
echo "  tail -f logs/*.log             # Individual notebook logs"
echo "  ls -lh outputs/executed_notebooks/  # Check output files"
echo ""
echo "=========================================="
echo "Check Status:"
echo "=========================================="
echo "  ps -fp $PID                    # Check if running"
echo "  cat run.pid                    # Get PID"
echo ""
echo "=========================================="
echo "Stop Execution:"
echo "=========================================="
echo "  kill $PID"
echo "  # or"
echo "  kill \$(cat run.pid)"
echo ""
echo "You can now safely close this terminal/browser tab!"
echo ""
