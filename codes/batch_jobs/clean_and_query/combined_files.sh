#!/bin/bash

PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
OPATH="/home/3302/hf_py_code/compile/codes/results/"
#types=("c" "cpp" "julia" "rust1" "rust2" "rust3" "rust4" "swift")
types=("c")
for lang in "${types[@]}"; do
  file_count=$(ls -1 "${PREFIX}${lang}/textseg_sizes/" | wc -l)
  output_lines=()
  echo "name,text_segment_size,instructions" >> "${OPATH}${lang}_text_segments.csv"
  for ((i=1; i<=$file_count; i++)); do
    output_lines+=$(awk -F, 'NR==FNR{a[NR]=$1","$2; next} {print a[FNR], $2}' \
    OFS=, ${PREFIX}${lang}/textseg_sizes/textseg${i}.csv \
    ${PREFIX}${lang}/instruction_counts/inst${i}.csv)
#    ${PREFIX}${lang}/instruction_counts/inst${i}.csv \
#    >> combined_output.csv
  done
#  echo ${output_lines[@]}
echo ${#output_lines[@]}
#    for line in "${output_lines[@]}"; do
#      echo "$line" >> "second_combined_output.csv"
#      echo "$line"
#    done
done

  #echo "text_segment_size" >> "${OPATH}${lang}_text_segments.csv"
#  echo "instructions" >> "${OPATH}${lang}_instructions.csv"
#    awk -F, '{print $2}' \
#    "${PREFIX}${lang}/textseg_sizes/textseg${i}.csv" \
#    >> "${OPATH}${lang}_text_segments.csv"
#    awk -F, '{print $2}' \
#    "${PREFIX}${lang}/instruction_counts/inst${i}.csv" \
#    >> "${OPATH}${lang}_instructions.csv"
