#!/bin/bash -l
#
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=12
#SBATCH --job-name=dataset_download
#SBATCH --partition=standard
#SBATCH --time=0-02:00:00
#SBATCH --export=NONE
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.out

python3.12 multi_tar_download.py
