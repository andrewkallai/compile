#!/bin/bash
PREFIX=/lustre/schandra_crpl/users/3302/ir_bc_files/
HOME_PRE=/home/3302/hf_py_code/compile/codes/batch_jobs/generators/

#language=("c" "cpp" "julia" "rust1" "rust2" "rust3" "rust4" "swift")

if [ -z $1 ]; then
  echo "Missing language argument." 
  exit 1
fi

data_type=("job_results" "results") 

if [ -n "$2" ]; then
  data_type+=("ps_*")
fi

declare -a strings

for result in "${data_type[@]}"; do
  strings+=("$1/${result}")
done


targets="${strings[@]}"
scancel -u andrewka
rm ${HOME_PRE}job_numbers.txt
touch ${HOME_PRE}job_numbers.txt
cd ${PREFIX}

rm -r ${targets}
targets=${targets//"$1/ps_*"/}
mkdir ${targets}

