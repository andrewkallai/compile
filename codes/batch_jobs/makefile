BC_FILES := $(wildcard bitcode_files/*.bc)

OBJ_FILES := $(patsubst bitcode_files/%.bc, test_out/%.o, $(BC_FILES))

all: $(OBJ_FILES)

test_out/%.o: bitcode_files/%.bc
	@/usr/bin/time -o time_out/$*.txt clang -O3 -c $< -o $@
