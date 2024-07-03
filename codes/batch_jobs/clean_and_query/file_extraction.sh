#!/bin/bash

PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
OPATH="/home/3302/hf_py_code/compile/codes/results/"
types=("c" "cpp" "julia" "rust1" "rust2" "rust3" "rust4" "swift")
#types=("c")
for lang in "${types[@]}"; do
  file_count=$(ls -1 "${PREFIX}${lang}/textseg_sizes/" | wc -l)
  echo "text_segment_size" >> "${OPATH}${lang}_text_segments.csv"
  echo "instructions" >> "${OPATH}${lang}_instructions.csv"
  for ((i=1; i<=$file_count; i++)); do
    awk -F, '{print $2}' \
    "${PREFIX}${lang}/textseg_sizes/textseg${i}.csv" \
    >> "${OPATH}${lang}_text_segments.csv"
    awk -F, '{print $2}' \
    "${PREFIX}${lang}/instruction_counts/inst${i}.csv" \
    >> "${OPATH}${lang}_instructions.csv"
  done
done

