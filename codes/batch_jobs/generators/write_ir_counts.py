from llvm_ir_dataset_utils.util.bitcode_module import get_fields_total_counts
import argparse

parser = argparse.ArgumentParser(description="Process a bitcode file and print field counts.")
parser.add_argument('filename', type=str, help="Path to the bitcode (.bc) file")


#FILE_NAME="/home/3302/hf_py_code/compile/codes/batch_jobs/generators/testing/bc_files/file2.bc"
print(', '.join(get_fields_total_counts(open(parser.parse_args().filename, "rb").read())))
#print(', '.join(get_fields_total_counts(open(parser.parse_args().filename, "rb").read(), names=True)))

