# Runtime Environment

## HPC Environment
- Cluster: On-prem HPC
- Scheduler: Slurm
- Filesystem: Lustre
- Execution Nodes: cpu partition

## Python
- Version: Python 3.12.4
- Virtual Environment: venv (user-space)

## Execution Policy
- No compute on master node
- All executions via Slurm
- Lustre is the only writable workspace
