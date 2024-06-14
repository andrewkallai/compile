#!/bin/bash
start=1
end=31653
#end=2
PREFIX="/lustre/schandra_crpl/users/3302/ir_bc_files/"
TYPE="c"

echo "${TYPE}" >> job_numbers.txt
date >> job_numbers.txt
for (( i=$start; i<=$end; i++ ))
do
    cp template1.qs p_$i.sh
    echo "#SBATCH \
    --output=${PREFIX}${TYPE}_result/${i}-%j.out" \
    >> p_${i}.sh
    echo "#SBATCH \
    --error=${PREFIX}${TYPE}_result/${i}-%j.out" \
    >> p_${i}.sh
    cat template2.qs >> p_$i.sh
    echo "clang -O3 -c -o \
    ${PREFIX}${TYPE}_out/file${i}.o ${PREFIX}${TYPE}/file${i}.bc" \
    >> p_${i}.sh
    echo "rm p_${i}.sh" >> p_${i}.sh
    #cat p_$i.sh
    while true; do
      sbatch p_${i}.sh >> job_numbers.txt
      if [ $? -ne 0 ]; then
       echo "sbatch failed. Sleeping for 1 second..."
       sleep 1
      else
       echo "sbatch succeeded."
       break
      fi
    done
done
