#!/bin/bash -l
#
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8
#SBATCH --job-name=compiler_batch
#SBATCH --partition=standard
#SBATCH --time=0-00:20:00
#SBATCH --export=NONE
#SBATCH --array=0-399
#SBATCH --mem=499712M
#SBATCH --output=/lustre/schandra_crpl/users/3302/ir_bc_files/rust/job_results/slurm-%A_%a.out
#SBATCH --error=/lustre/schandra_crpl/users/3302/ir_bc_files/rust/job_results/slurm-%A_%a.out
START=144641
TYPE=rust
SIZE=209059
STORAGE=/lustre/schandra_crpl/users/3302/ir_bc_files
TEMP_DIR=/tmp
MAKE_PATH=/home/3302/hf_py_code/compile/compile_time_analysis_tools
THREADS=24
export PYTHONPATH="/home/3302/llvm-ir-dataset-utils:"

set -o errexit
DATA_NAMES=("text_segment" "instruction" "ir_features" "max_pass")
if [ -z "$SLURM_JOB_ID" ]; then
  I=$((${START}+1))
  STOP=$(($I+${SIZE}-1))
else
  BATCH=$(($SIZE/$SLURM_ARRAY_TASK_MAX))
  I=$((${SLURM_ARRAY_TASK_ID}*${BATCH}+1+${START}))
  STOP=$(($I+${BATCH}-1))
  if [ $SLURM_ARRAY_TASK_ID -eq $SLURM_ARRAY_TASK_MAX ]; then
    STOP=$(($I+${SIZE}%$SLURM_ARRAY_TASK_MAX-1))
  fi
fi

cd ${TEMP_DIR}
mkdir -p ir_bc_files/ps_$I/${TYPE}
cd ir_bc_files/ps_$I/${TYPE}
mkdir -p bc_files ${DATA_NAMES[1]}_counts perf_stat_files \
  ${DATA_NAMES[0]}_counts ${DATA_NAMES[2]}_counts \
  ${DATA_NAMES[3]}_counts object_files

eval tar --extract --file=${STORAGE}/${TYPE}/${TYPE}_bc_files.tar \
  bc_files/file{$I..$STOP}.bc

cd ..
make --ignore-errors --makefile=${MAKE_PATH}/Makefile \
  --jobs=${THREADS} lang="${TYPE}" begin="$I" end="$STOP"

TARGET_DIR="${STORAGE}/${TYPE}/ps_$I"
mkdir -p $TARGET_DIR

for element in "${DATA_NAMES[@]}"; do
  > ${TARGET_DIR}/${element}.csv
  eval cat ${TYPE}/${element}_counts/${element}{$I..$STOP}.csv \
  >> ${TARGET_DIR}/${element}.csv
done

cd ..
rm -r ps_$I
