#!/bin/bash
#SBATCH --job-name=fuel-opt-array
#SBATCH --partition=cpu
#SBATCH --array=0-1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:20:00
#SBATCH --output=logs/scheduler/%x_%A_%a.out
#SBATCH --error=logs/scheduler/%x_%A_%a.err

set -euo pipefail

PROJECT_ROOT=/lustre/mansoor.wani/projects/airline-fuel-optimization-agent
VENV_PATH=$PROJECT_ROOT/.venv

source $VENV_PATH/bin/activate
cd $PROJECT_ROOT

python -m app.hpc.flight_task $SLURM_ARRAY_TASK_ID \
  > logs/application/task_${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}.log
