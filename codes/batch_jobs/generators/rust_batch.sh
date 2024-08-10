#!/bin/bash -l
#
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=12
#SBATCH --job-name=compiler_batch
#SBATCH --partition=standard
#SBATCH --time=0-00:10:00
#SBATCH --export=NONE
# NUMBER OF JOBS: 400
#SBATCH --array=0-399

#SBATCH --output=/lustre/schandra_crpl/users/3302/ir_bc_files/rust/job_results/slurm-%A_%a.out
#SBATCH --error=/lustre/schandra_crpl/users/3302/ir_bc_files/rust/job_results/slurm-%A_%a.out
START=144641
TYPE=rust
SIZE=209059
STORAGE=/lustre/schandra_crpl/users/3302/ir_bc_files
MAKE_PATH=/home/3302/hf_py_code/compile/codes/batch_jobs/makefile_dir
THREADS=24
BATCH=$(($SIZE/$SLURM_ARRAY_TASK_MAX))
I=$((${SLURM_ARRAY_TASK_ID}*${BATCH}+1+${START}))
STOP=$(($I+${BATCH}-1))
if [ $SLURM_ARRAY_TASK_ID -eq $SLURM_ARRAY_TASK_MAX ]; then
  STOP=$(($I+${SIZE}%$SLURM_ARRAY_TASK_MAX-1))
fi
cd $TMPDIR
mkdir -p ir_bc_files/ps_$I/${TYPE}
cd ir_bc_files/ps_$I/${TYPE}
mkdir -p bc_files instruction_counts perf_stat_files \
  textseg_sizes object_files
eval tar --extract --file=${STORAGE}/${TYPE}/${TYPE}_bc_files.tar \
  bc_files/file{$I..$STOP}.bc
cd $TMPDIR/ir_bc_files/ps_$I
make --ignore-errors --makefile=${MAKE_PATH}/Makefile \
  --jobs=${THREADS} lang="${TYPE}" begin="$I" end="$STOP"
mkdir -p ${STORAGE}/${TYPE}/ps_$I
> ${STORAGE}/${TYPE}/ps_$I/text_segments.csv

> ${STORAGE}/${TYPE}/ps_$I/instructions.csv

eval cat ${TYPE}/textseg_sizes/textseg{$I..$STOP}.csv \
  >> ${STORAGE}/${TYPE}/ps_$I/text_segments.csv
eval cat ${TYPE}/instruction_counts/inst{$I..$STOP}.csv \
  >> ${STORAGE}/${TYPE}/ps_$I/instructions.csv
cd ..
rm -r ps_$I

