#!/bin/bash
PREFIX=/lustre/schandra_crpl/users/3302/ir_bc_files/

language=("c" "cpp" "julia" "rust" "swift")

#data_type=("job_results" "object_files" "perf_stat_files" \
#"instruction_counts" "textseg_sizes" "results")

declare -a strings

for dir in "${language[@]}"; do
  for result in "${data_type[@]}"; do
    strings+=("${dir}/${result}")
  done
done

cd ${PREFIX}
targets="${strings[@]}"

#for dir in "${strings[@]}"; do
for dir in "${language[@]}"; do
    echo -n "${dir} ps_ count "
#    ls -1 ${PREFIX}${dir}/ | wc -l
    find ${PREFIX}${dir}/ -name "ps_*" | wc -l
    echo -n "job_results "
    ls -1 ${PREFIX}${dir}/job_results/ | wc -l
done

