# -*- coding: ascii -*-
# download.py
from datasets import load_dataset

ds = load_dataset('llvm-ml/ComPile', split='train')
#ds = load_dataset('llvm-ml/ComPile', split='train', columns=['content'])

