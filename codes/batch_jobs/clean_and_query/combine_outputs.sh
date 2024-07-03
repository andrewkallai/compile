#!/bin/bash
PREFIX=/lustre/schandra_crpl/users/3302/ir_bc_files/
#HOME_PRE=/home/3302/hf_py_code/compile/codes/results/

#language=("c" "cpp" "julia" "rust1" "rust2" "rust3" "rust4" "swift")
#language=("cpp")
language=($1)
if [ ${#language[@]} -eq 0 ]; then
  echo "Missing language argument." 
  exit 1
fi

cd ${PREFIX}
for dir in "${language[@]}"; do
  echo "file, text_segment_size" \
  > ${dir}/results/${dir}_text_segments.csv
  echo "file, instructions" \
  > ${dir}/results/${dir}_instructions.csv
#  echo "file,text_segment_size" > "${PREFIX}${dir}/results/${dir}_text_segments.csv"
#  echo "file,instructions" > "${PREFIX}${dir}/results/${dir}_instructions.csv"
  for ps in ${dir}/ps_*; do 
#    (find ${ps}/textseg_sizes | xargs cat) \
    cat ${ps}/text_segments.csv \
    >> ${dir}/results/${dir}_text_segments.csv
#    (find ${ps}/instruction_counts | xargs cat) \
    cat ${ps}/instructions.csv \
    >> ${dir}/results/${dir}_instructions.csv


#  echo "$(find ${dir}/textseg_sizes | xargs cat), \
#  $(find ${dir}/instruction_counts | xargs cat)" \
#  >> ${HOME_PRE}${dir}_combined.csv
  done
  sort -nk1.5 ${dir}/results/${dir}_text_segments.csv \
  -o ${dir}/results/${dir}_text_segments.csv
  sort -nk1.5 ${dir}/results/${dir}_instructions.csv \
  -o ${dir}/results/${dir}_instructions.csv
  awk -F, 'NR==FNR{a[NR]=$1","$2; next} {print a[FNR], $2}' \
  OFS=, ${dir}/results/${dir}_text_segments.csv \
  ${dir}/results/${dir}_instructions.csv \
  > ${dir}/results/${dir}_combined_results.csv
  rm ${dir}/results/${dir}_instructions.csv \
  ${dir}/results/${dir}_text_segments.csv 
  rm -r ${dir}/ps_*
done
