#!/bin/bash
#SBATCH --partition computeq
#SBATCH --cpus-per-task 1

function echoMe {
    echo "Hello $1 from job $SLURM_JOB_ID"
    sleep 120
    exit 0
}
