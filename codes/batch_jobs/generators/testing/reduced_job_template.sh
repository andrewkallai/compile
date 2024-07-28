#!/bin/bash -l
#
#SBATCH --nodes=1 --ntasks=1
#SBATCH --job-name=compiler_batch
#SBATCH --partition=standard
#SBATCH --time=0-00:10:00
#SBATCH --export=NONE
#SBATCH --array=0-1
#SBATCH --output=/lustre/schandra_crpl/users/3302/ir_bc_files/testing/job_results/slurm-%A_%a.out
#SBATCH --error=/lustre/schandra_crpl/users/3302/ir_bc_files/testing/job_results/slurm-%A_%a.out
#
