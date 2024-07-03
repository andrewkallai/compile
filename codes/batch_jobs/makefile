SHELL := /bin/bash

WILD := $(shell echo {$(begin)..$(end)})

WILD := $(filter-out 24761,$(WILD))

CC := clang

ifeq ($(lang), cpp)
    CC := clang++ 
endif

all: $(WILD) 

$(WILD):
#	@size=$$(perf stat --no-big-num -e instructions \
    -o $(lang)/perf_stat_files/file$@.txt clang -O3 -c $(lang)/bc_files/file$@.bc -o - \
    | llvm-size - | awk 'NR==2 {print $$1}'); \
    echo "file$@, $$size" >> $(lang)/textseg_sizes/textseg$@.csv
	@perf stat --no-big-num -e instructions -o \
		$(lang)/perf_stat_files/file$@.txt \
  	$(CC) -O3 -c $(lang)/bc_files/file$@.bc \
		-o $(lang)/object_files/file$@.o
#	@perf stat --no-big-num -e instructions -o \
		$(lang)/perf_stat_files/file$@.txt \
  	opt -O3 $(lang)/bc_files/file$@.bc \
		-o $(lang)/object_files/file$@.o
	@instruct=$$(awk '/instructions/ {print $$1}' \
		$(lang)/perf_stat_files/file$@.txt); \
		echo "file$@, $$instruct" >> $(lang)/instruction_counts/inst$@.csv
	@size=$$(llvm-size $(lang)/object_files/file$@.o | awk 'NR==2 {print $$1}'); \
		echo "file$@, $$size" >> $(lang)/textseg_sizes/textseg$@.csv

