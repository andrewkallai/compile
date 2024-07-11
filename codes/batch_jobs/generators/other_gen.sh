#!/bin/bash

#lang=("c" "cpp" "julia" "rust1" "rust2" "rust3" "rust4" "swift")
lang=("c" "cpp" "julia" "rust" "swift")
#array1=(1 31654 87226 144642 209642 274642 339642 353701)
array1=(1 31654 87226 144642 353701)
#array2=(31653 87225 144641 209641 274641 339641 353700 402751)
array2=(31653 87225 144641 353700 402751)
#batch_sizes=(80 140 145 165 165 165 40 125)
batch_sizes=(80 139 144 523 123)
array_sizes=(395 399 398 399 398)
#batch_sizes=(80 139 144 523 123)

length=${#lang[@]}
cd /home/3302/hf_py_code/compile/codes/batch_jobs/generators

for (( i=0; i<$length; i++ ))
do
     > ${lang[$i]}_generator.sh
    echo "#!/bin/bash" >> ${lang[$i]}_generator.sh
    echo "start=${array1[$i]}" >> ${lang[$i]}_generator.sh
    echo "end=${array2[$i]}" >> ${lang[$i]}_generator.sh
    echo "TYPE=${lang[$i]}" >> ${lang[$i]}_generator.sh
    echo "batch_size=${batch_sizes[$i]}" >> ${lang[$i]}_generator.sh
    echo "array_size=${array_sizes[$i]}" >> ${lang[$i]}_generator.sh
    cat array_launcher_template.sh>> ${lang[$i]}_generator.sh
    chmod 744 ${lang[$i]}_generator.sh 
done
