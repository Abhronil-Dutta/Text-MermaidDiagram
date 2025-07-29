
import torch
import transformers
from sentence_transformers import SentenceTransformer
import pandas as pd
import matplotlib.pyplot as plt

print("PyTorch version:", torch.__version__)
print("Transformers version:", transformers.__version__)
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Loaded sentence-transformer:", model)
df = pd.DataFrame({'a': [1,2], 'b': [3,4]})
print("Pandas DataFrame shape:", df.shape)
plt.figure(); plt.plot([0,1],[1,0]); plt.close()
print("Everything imported successfully.")
