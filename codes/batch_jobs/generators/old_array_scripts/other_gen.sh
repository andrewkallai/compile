#!/bin/bash

lang=("c" "cpp" "julia" "rust" "swift")
array1=(0 31653 87225 144641 353700)
#array1=(1 31654 87226 144642 353701)
array2=(31653 87225 144641 353700 402751)
batch_sizes=(79 138 143 522 122)

length=${#lang[@]}
cd /home/3302/hf_py_code/compile/codes/batch_jobs/generators

for (( i=0; i<$length; i++ ))
do
     > ${lang[$i]}_generator.sh
    echo "#!/bin/bash" >> ${lang[$i]}_generator.sh
    echo "START=${array1[$i]}" >> ${lang[$i]}_generator.sh
    echo "end=${array2[$i]}" >> ${lang[$i]}_generator.sh
    echo "TYPE=${lang[$i]}" >> ${lang[$i]}_generator.sh
    echo "batch_size=${batch_sizes[$i]}" >> ${lang[$i]}_generator.sh
    cat array_launcher_template.sh>> ${lang[$i]}_generator.sh
    chmod 744 ${lang[$i]}_generator.sh 
done
