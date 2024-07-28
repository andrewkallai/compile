if [ -z $1 ]; then
  echo "Missing STORAGE argument."
  exit 1
fi
#if [ -z $2 ]; then
#  echo "Missing MAKEFILE argument."
#  exit 1
#fi
STORAGE="/lustre/schandra_crpl/users/3302/ir_bc_files/"
#STORAGE="$1"
BATCH_PATH="/home/3302/hf_py_code/compile/codes/batch_jobs/makefile_dir/"
#MAKEFILE="$2"
exit 1
cd /home/3302/hf_py_code/compile/codes/batch_jobs/generators
echo "${TYPE}" >> job_numbers.txt
date >> job_numbers.txt
js="main_p.sh"
cp job_template.sh $js
echo "#SBATCH \
--output=${PREFIX}${TYPE}/job_results/slurm-%A_%a.out" >> $js
echo "#SBATCH \
--error=${PREFIX}${TYPE}/job_results/slurm-%A_%a.out" >> $js

echo "#SBATCH --array=0-399" >> $js
cat setup_portion.sh >> $js

echo "I=\$((\$SLURM_ARRAY_TASK_ID*${batch_size}+1+${START}))" >> ${js}
echo "STOP=\$((\$I+${batch_size}-1+${START}))" >> ${js}
echo "if [ \$SLURM_ARRAY_TASK_ID -eq 399 ]; then" >> ${js}
echo "  STOP=\$((\$I+${end}%399-1+${START}))" >> ${js}
echo "fi" >> ${js}
echo "cd /tmp" >> ${js}
echo "mkdir -p ir_bc_files/ps_\$I/${TYPE}" >> ${js}
echo "cd ir_bc_files/ps_\$I/${TYPE}" >> ${js}
echo "mkdir -p bc_files instruction_counts perf_stat_files \
textseg_sizes object_files" >> ${js}
echo "eval tar --extract --file=${PREFIX}${TYPE}/${TYPE}_bc_files.tar \
bc_files/file{\$I..\$STOP}.bc" >> ${js}
echo "cd /tmp/ir_bc_files/ps_\$I" >> ${js}
echo "make -f ${BATCH_PATH}no_ignore_error_makefile \
-j 64 lang="${TYPE}" begin="\$I" \
end="\$STOP"" >> ${js}
echo "mkdir -p ${PREFIX}${TYPE}/ps_\$I" >> ${js}
echo " > ${PREFIX}${TYPE}/ps_\$I/text_segments.csv" \
>> ${js}
echo " > ${PREFIX}${TYPE}/ps_\$I/instructions.csv" \
>> ${js}
echo "eval cat ${TYPE}/textseg_sizes/textseg{\$I..\$STOP}.csv \
>> ${PREFIX}${TYPE}/ps_\$I/text_segments.csv" >> ${js}
echo "eval cat ${TYPE}/instruction_counts/inst{\$I..\$STOP}.csv \
>> ${PREFIX}${TYPE}/ps_\$I/instructions.csv" >> ${js}
echo "cd .." >> ${js}
echo "rm -r ps_\$I" >> ${js}

