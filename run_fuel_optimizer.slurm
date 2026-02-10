#!/bin/bash
#SBATCH --job-name=fuel-opt
#SBATCH --partition=cpu
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=logs/scheduler/%x_%j.out
#SBATCH --error=logs/scheduler/%x_%j.err

# Fail immediately on errors
set -euo pipefail

# Absolute paths for reproducibility
PROJECT_ROOT=/lustre/mansoor.wani/projects/airline-fuel-optimization-agent
VENV_PATH=$PROJECT_ROOT/.venv

# Activate environment
source $VENV_PATH/bin/activate

# Move to project root
cd $PROJECT_ROOT

# Run application and capture logs
python app/main.py > logs/application/run_${SLURM_JOB_ID}.log
