#!/bin/bash
start=31654
end=87225
TYPE=cpp
batch_size=139
array_size=399
PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
BATCH_PATH="/home/3302/hf_py_code/compile/codes/batch_jobs/makefile_dir/"

cd /home/3302/hf_py_code/compile/codes/batch_jobs/generators
echo "${TYPE}" >> job_numbers.txt
date >> job_numbers.txt
js="main_p.sh"
cp job_template.sh $js
echo "#SBATCH \
--output=${PREFIX}${TYPE}/job_results/slurm-%A_%a.out" >> $js
echo "#SBATCH \
--error=${PREFIX}${TYPE}/job_results/slurm-%A_%a.out" >> $js

#echo "#SBATCH --array=${values}" >> $js
#echo "#SBATCH --array=${start}-${end}:${batch_size}" >> $js
#echo "#SBATCH --array=0-9999" >> $js
echo "#SBATCH --array=0-${array_size}" >> $js
#echo "#SBATCH --array=0-59" >> $js
cat setup_portion.sh >> $js

#    STOP=$((i+batch_size-1))
#    if [ $STOP -gt ${end} ]; then
#      STOP=${end} 
#    fi
#100000
#echo "I=\$SLURM_ARRAY_TASK_ID" >> ${js}
echo "I=\$((\$SLURM_ARRAY_TASK_ID*${batch_size}+1))" >> ${js}
#echo "if [ \$I -eq 0 ]; then" >> ${js}
#echo "  I=1" >> ${js}
#echo "fi" >> ${js}
echo "STOP=\$((\$I+${batch_size}-1))" >> ${js}
echo "if [ \$STOP -gt ${end} ]; then" >> ${js}
echo "  STOP=${end}" >> ${js}
echo "fi" >> ${js}
echo "cd /tmp" >> ${js}
echo "mkdir -p ir_bc_files/ps_\$I/${TYPE}" >> ${js}
echo "cd ir_bc_files/ps_\$I/${TYPE}" >> ${js}
echo "mkdir -p bc_files instruction_counts perf_stat_files \
textseg_sizes object_files" >> ${js}
echo "eval tar --extract --file=${PREFIX}${TYPE}/${TYPE}_bc_files.tar \
bc_files/file{\$I..\$STOP}.bc" >> ${js}
echo "cd /tmp/ir_bc_files/ps_\$I" >> ${js}
#echo "srun make -f ${BATCH_PATH}no_ignore_error_makefile \
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

#while true; do
#        sbatch ${js} >> job_numbers.txt
#    if [ $? -ne 0 ]; then
#        squeue -u andrewka --states=PD --noheader | wc -l
#        echo "sbatch failed. Sleeping for 1 second..."
#        sleep 1
#    else
#        break
#    fi
#done
#    rm ${js}
#done

