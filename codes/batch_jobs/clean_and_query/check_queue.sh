#!/bin/bash

while true; do
  count=$(squeue -u andrewka --noheader | wc -l)
  if [ $count -ne 0 ]; then
    sleep 2
  else
    break
  fi
done
