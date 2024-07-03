#!/bin/bash

while true; do
  sbatch dummy_batch.sh
  if [ $? -ne 0 ]; then
    count=$(squeue -u andrewka --noheader | wc -l)
    echo ${count}
    break
  fi
done
