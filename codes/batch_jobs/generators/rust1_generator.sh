#!/bin/bash
start=144642
end=209641
TYPE=rust1
batch_size=165
PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
BATCH_PATH="/home/3302/hf_py_code/compile/codes/batch_jobs/"
cd /home/3302/hf_py_code/compile/codes/batch_jobs/generators
echo "${TYPE}" >> job_numbers.txt
date >> job_numbers.txt

for (( i=$start; i<=$end; i+=$batch_size ))
do
    js="p_${i}.sh"
    cp template1.sh $js
    echo "#SBATCH \
    --output=${PREFIX}${TYPE}/job_results/${i}-%j.out" >> $js
    echo "#SBATCH \
    --error=${PREFIX}${TYPE}/job_results/${i}-%j.out" >> $js
    cat template2.sh >> $js

    STOP=$((i+batch_size-1))
    if [ $STOP -gt ${end} ]; then
      STOP=${end} 
    fi
   
    echo "cd /tmp" >> ${js}
    echo "mkdir -p ir_bc_files/ps_${i}/${TYPE}" >> ${js}
    echo "cd ir_bc_files/ps_${i}/${TYPE}" >> ${js}
    echo "mkdir -p bc_files instruction_counts perf_stat_files \
    textseg_sizes object_files" >> ${js}
    echo "tar --extract --file=${PREFIX}${TYPE}/${TYPE}_bc_files.tar \
    bc_files/file{${i}..${STOP}}.bc" >> ${js}
    echo "cd /tmp/ir_bc_files/ps_${i}" >> ${js}
    echo "make -f ${BATCH_PATH}makefile -j 64 \
    lang="${TYPE}" begin="${i}" \
    end="${STOP}"" >> ${js}
    echo "mkdir -p ${PREFIX}${TYPE}/ps_${i}" >> ${js}
    echo " > ${PREFIX}${TYPE}/ps_${i}/text_segments.csv" \
    >> ${js}
    echo " > ${PREFIX}${TYPE}/ps_${i}/instructions.csv" \
    >> ${js}
    echo "cat ${TYPE}/textseg_sizes/textseg{${i}..${STOP}}.csv \
    >> ${PREFIX}${TYPE}/ps_${i}/text_segments.csv" >> ${js}
    echo "cat ${TYPE}/instruction_counts/inst{${i}..${STOP}}.csv \
    >> ${PREFIX}${TYPE}/ps_${i}/instructions.csv" >> ${js}
    echo "cd .." >> ${js}
    echo "rm -r ps_${i}" >> ${js}

    while true; do
        sbatch ${js} >> job_numbers.txt
        if [ $? -ne 0 ]; then
            squeue -u andrewka --states=PD --noheader | wc -l
            echo "sbatch failed. Sleeping for 1 second..."
            sleep 1
        else
            break
        fi
    done
    rm ${js}
done

