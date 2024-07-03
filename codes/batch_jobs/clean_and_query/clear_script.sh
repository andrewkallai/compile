#!/bin/bash
PREFIX=/lustre/schandra_crpl/users/3302/ir_bc_files/
HOME_PRE=/home/3302/hf_py_code/compile/codes/batch_jobs/generators/

language=("c" "cpp" "julia" "rust1" "rust2" "rust3" "rust4" "swift")

data_type=("job_results" "object_files" "perf_stat_files" \
"instruction_counts" "textseg_sizes" "results")

declare -a strings

#for dir in "${language[@]}"; do
  for result in "${data_type[@]}"; do
    strings+=("$1/${result}")
  done
#done


targets="${strings[@]}"
scancel -u andrewka
rm ${HOME_PRE}job_numbers.txt
touch ${HOME_PRE}job_numbers.txt

cd ${PREFIX}
rm -r ${targets}
mkdir ${targets}

