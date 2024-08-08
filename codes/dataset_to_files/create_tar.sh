#!/bin/bash

#Usage:
#create_tar.sh <language> [storage]

if [ -z "$1" ]; then
  echo "Missing language argument."
  exit 1
else
  LANGUAGE="$1"
fi

if [ -z "$2" ]; then
  STORAGE="/tmp/test_storage"
else
  STORAGE="$2"
fi

cd ${STORAGE}/${LANGUAGE}

for dir in [0-9]*_temp; do
  cd $dir
#  tar --create --file="../${dir}.tar" \
#  --transform=s,^,bc_files/, file[0-9]*.bc
  tar --append --file="../${LANGUAGE}_bc_files.tar" \
  --transform=s,^,bc_files/, file[0-9]*.bc
  cd ..
#  tar --concatenate --file="${LANGUAGE}_bc_files.tar" "${dir}.tar"

#  rm -r "${dir}.tar" "${dir}"
  rm -r "${dir}"
done

