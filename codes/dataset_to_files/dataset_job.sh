#!/bin/bash -l
#
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=12
#SBATCH --job-name=datasetdownload
#SBATCH --partition=xlarge-mem
# SBATCH –-mem=2031616M
#SBATCH --mem=2031616M
#SBATCH --time=0-02:00:00
#SBATCH --export=NONE
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.out

python3.12 multi_tar_download.py
