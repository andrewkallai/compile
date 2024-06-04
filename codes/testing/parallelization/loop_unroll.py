from datasets import load_dataset, parallel
with parallel.parallel_backend('spark'):
  ds = load_dataset("llvm-ml/ComPile", split="train[0:1000]", num_proc=2)
for i in range(0,len(ds["content"])):
  print('run_subprocess(ds[\"content\"]['+str(i)+']),')
# run_subprocess(ds["content"][0])
