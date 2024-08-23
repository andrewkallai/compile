#!/bin/bash

# Initialize an associative array
declare -A analysis_results

# Sample input data (replace with actual input if needed)
input_data="Printing analysis results of CFA for function 'FLA_Trsm_llt_blk_var2':
BasicBlockCount: 4
BlocksReachedFromConditionalInstruction: 2
Uses: 1
DirectCallsToDefinedFunctions: 0
LoadInstCount: 12
StoreInstCount: 3
MaxLoopDepth: 1
TopLevelLoopCount: 1
TotalInstructionCount: 57
BasicBlocksWithSingleSuccessor: 2
BasicBlocksWithTwoSuccessors: 1
BasicBlocksWithMoreThanTwoSuccessors: 0
BasicBlocksWithSinglePredecessor: 2
BasicBlocksWithTwoPredecessors: 1
BasicBlocksWithMoreThanTwoPredecessors: 0
BigBasicBlocks: 0
MediumBasicBlocks: 4
SmallBasicBlocks: 0
CastInstructionCount: 0
FloatingPointInstructionCount: 0
IntegerInstructionCount: 17
ConstantIntOperandCount: 45
ConstantFPOperandCount: 0
ConstantOperandCount: 0
InstructionOperandCount: 80
BasicBlockOperandCount: 4
GlobalValueOperandCount: 15
InlineAsmOperandCount: 0
ArgumentOperandCount: 7
UnknownOperandCount: 0
CriticalEdgeCount: 0
ControlFlowEdgeCount: 4
UnconditionalBranchCount: 2
IntrinsicCount: 0
DirectCallCount: 12
IndirectCallCount: 0
CallReturnsIntegerCount: 12
CallReturnsFloatCount: 0
CallReturnsPointerCount: 0
CallReturnsVectorIntCount: 0
CallReturnsVectorFloatCount: 0
CallReturnsVectorPointerCount: 0
CallWithManyArgumentsCount: 8
CallWithPointerArgumentCount: 12"

# Read each line of input data
while IFS= read -r line; do
    # Use regex to match the key-value pair
    if [[ $line =~ ^([a-zA-Z0-9_]+):\ ([0-9]+)$ ]]; then
        key="${BASH_REMATCH[1]}"
        value="${BASH_REMATCH[2]}"
        # Add to the associative array
        analysis_results[$key]=$value
    fi
done <<< "$input_data"

# Print the associative array (for verification)
for key in "${!analysis_results[@]}"; do
    echo "$key: ${analysis_results[$key]}"
done

