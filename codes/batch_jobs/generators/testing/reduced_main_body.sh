START=0
TYPE=testing
SIZE=31653
STORAGE=/lustre/schandra_crpl/users/3302/ir_bc_files/
BATCH_PATH=/home/3302/hf_py_code/compile/codes/batch_jobs/makefile_dir/
BATCH=$(($SIZE/399))
I=$((${SLURM_ARRAY_TASK_ID}*${BATCH}+1+${START}))
STOP=$(($I+${BATCH}-1))
if [ $SLURM_ARRAY_TASK_ID -eq $SLURM_ARRAY_TASK_MAX ]; then
  STOP=$(($I+${SIZE}%399-1))
fi
cd $STORAGE
#echo $I $STOP
time make --ignore-errors --makefile=${BATCH_PATH}no_ignore_error_makefile \
--jobs=32 lang="${TYPE}" begin="$I" end="$STOP"
