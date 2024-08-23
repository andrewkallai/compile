#!/bin/bash
set -o errexit
#Usage:
#./combine_outputs.sh <language> [storage]

if [ -z "$1" ]; then
  echo "Missing language argument."
  exit 1
else
  LANGUAGE="$1"
fi

if [ -z "$2" ]; then
  STORAGE="/lustre/schandra_crpl/users/3302/ir_bc_files"
else
  STORAGE="$2"
fi


cd ${STORAGE}

mkdir -p ${LANGUAGE}/results
TARGET_PREFIX="${LANGUAGE}/results/${LANGUAGE}"

create_files ()
{
  echo "file, text_segment_size" \
  > ${TARGET_PREFIX}_
}
boolean=1

DATA_NAMES=("text_segment" "instruction" "ir_features" "max_pass")
#DATA_NAMES=("text_segment" "instruction")
for element in "${DATA_NAMES[@]}"; do
  if [[ ${element} == ${DATA_NAMES[2]} ]]; then
#    python_output=$(python3.12 /home/3302/hf_py_code/compile/codes/batch_jobs/generators/write_ir_counts.py /dev/null)
#    echo "file, $python_output" \

    echo "file, BasicBlockCount, BlocksReachedFromConditionalInstruction, Uses, DirectCallsToDefinedFunctions, LoadInstCount, StoreInstCount, MaxLoopDepth, TopLevelLoopCount, TotalInstructionCount, BasicBlocksWithSingleSuccessor, BasicBlocksWithTwoSuccessors, BasicBlocksWithMoreThanTwoSuccessors, BasicBlocksWithSinglePredecessor, BasicBlocksWithTwoPredecessors, BasicBlocksWithMoreThanTwoPredecessors, BigBasicBlocks, MediumBasicBlocks, SmallBasicBlocks, CastInstructionCount, FloatingPointInstructionCount, IntegerInstructionCount, ConstantIntOperandCount, ConstantFPOperandCount, ConstantOperandCount, InstructionOperandCount, BasicBlockOperandCount, GlobalValueOperandCount, InlineAsmOperandCount, ArgumentOperandCount, UnknownOperandCount, CriticalEdgeCount, ControlFlowEdgeCount, UnconditionalBranchCount, IntrinsicCount, DirectCallCount, IndirectCallCount, CallReturnsIntegerCount, CallReturnsFloatCount, CallReturnsPointerCount, CallReturnsVectorIntCount, CallReturnsVectorFloatCount, CallReturnsVectorPointerCount, CallWithManyArgumentsCount, CallWithPointerArgumentCount" \
    > ${TARGET_PREFIX}_${element}.csv
  elif [[ ${element} == ${DATA_NAMES[3]} ]]; then
    echo "file, percentage, pass_name" \
    > ${TARGET_PREFIX}_${element}.csv
  else
    echo "file, ${element}" \
    > ${TARGET_PREFIX}_${element}.csv
  fi
  ls ${LANGUAGE}/ps_[0-9]*/${element}.csv | xargs cat \
  >> ${TARGET_PREFIX}_${element}.csv
#  for ps in ${LANGUAGE}/ps_*; do 
#    cat ${ps}/${element}.csv \
#    >> ${TARGET_PREFIX}_${element}.csv
#  done
  sort -nk1.5 ${TARGET_PREFIX}_${element}.csv \
  -o ${TARGET_PREFIX}_${element}.csv
  if [ $boolean -eq 1 ]; then
    awk -F',' '{print $1}' ${TARGET_PREFIX}_${DATA_NAMES[0]}.csv > ${TARGET_PREFIX}_combined.csv
    boolean=0
  fi
#  awk -F',' -v OFS=',' 'NR==FNR{newcol[NR]=$2; next} {print $0, newcol[FNR]}' \
#  awk -F',' -v OFS=',' '{for(i=2;i<=NF;i++) printf $i (i<NF?OFS:ORS)}' \
  awk -F',' -v OFS=',' 'NR==FNR {for (i=2; i<=NF; i++) cols[FNR]=(cols[FNR]?cols[FNR] OFS:"") $i; next} {print $0, cols[FNR]}' \
    ${TARGET_PREFIX}_${element}.csv \
    ${TARGET_PREFIX}_combined.csv \
    > ${TARGET_PREFIX}_temp.csv
  mv ${TARGET_PREFIX}_temp.csv ${TARGET_PREFIX}_combined.csv
#  rm ${TARGET_PREFIX}_${element}.csv
done
#sed -n -i '/, ,/!p' ${TARGET_PREFIX}_combined.csv

#rm -r ${LANGUAGE}/ps_*

#echo "file, text_segment_size" \
#  > ${LANGUAGE}/results/${LANGUAGE}_text_segments.csv
#echo "file, instructions" \
#  > ${LANGUAGE}/results/${LANGUAGE}_instructions.csv
#for ps in ${LANGUAGE}/ps_*; do 
#  cat ${ps}/text_segments.csv \
#    >> ${LANGUAGE}/results/${LANGUAGE}_text_segments.csv
#  cat ${ps}/instructions.csv \
#    >> ${LANGUAGE}/results/${LANGUAGE}_instructions.csv
#done
#sort -nk1.5 ${LANGUAGE}/results/${LANGUAGE}_text_segments.csv \
#  -o ${LANGUAGE}/results/${LANGUAGE}_text_segments.csv
#sort -nk1.5 ${LANGUAGE}/results/${LANGUAGE}_instructions.csv \
#  -o ${LANGUAGE}/results/${LANGUAGE}_instructions.csv
#awk -F, 'NR==FNR{a[NR]=$1","$2; next} {print a[FNR], $2}' \
#  OFS=, ${LANGUAGE}/results/${LANGUAGE}_text_segments.csv \
#  ${LANGUAGE}/results/${LANGUAGE}_instructions.csv \
#  > ${LANGUAGE}/results/${LANGUAGE}_combined_results.csv

#sed -n -i '/, ,/!p' ${LANGUAGE}/results/${LANGUAGE}_combined_results.csv

#rm ${LANGUAGE}/results/${LANGUAGE}_instructions.csv \
#  ${LANGUAGE}/results/${LANGUAGE}_text_segments.csv 

