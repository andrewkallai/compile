#!/bin/bash -l
#
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=12
#SBATCH --job-name=compiler_batch
#SBATCH --partition=standard
#SBATCH --time=0-00:10:00
#SBATCH --export=NONE
# SBATCH --array=0-1

#SBATCH --output=/lustre/schandra_crpl/users/3302/ir_bc_files/testing/job_results/slurm-%A_%a.out
#SBATCH --error=/lustre/schandra_crpl/users/3302/ir_bc_files/testing/job_results/slurm-%A_%a.out
START=0
TYPE=testing
SIZE=31653
STORAGE=/lustre/schandra_crpl/users/3302/ir_bc_files/
BATCH_PATH=/home/3302/hf_py_code/compile/codes/batch_jobs/makefile_dir/
#BATCH=$(($SIZE/$SLURM_ARRAY_TASK_MAX))
#I=$((${SLURM_ARRAY_TASK_ID}*${BATCH}+1+${START}))
#STOP=$(($I+${BATCH}-1))
#if [ $SLURM_ARRAY_TASK_ID -eq $SLURM_ARRAY_TASK_MAX ]; then
#  STOP=$(($I+${SIZE}%$SLURM_ARRAY_TASK_MAX-1))
#fi
cd $STORAGE
make --ignore-errors --makefile=${BATCH_PATH}no_ignore_error_makefile \
--jobs=32 lang="testing" begin="1" end="79"

