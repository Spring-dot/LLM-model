import faiss
import pandas as pd
import numpy as np

# Load embeddings
data = pd.read_pickle('data/bug_report_embeddings.pkl')

# Stack embeddings into a numpy array
embeddings = np.vstack(data['embeddings'].values)

# Create a FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save the FAISS index
faiss.write_index(index, 'data/bug_report_index.faiss')
