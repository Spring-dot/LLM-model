import faiss
import numpy as np
from transformers import BertModel, BertTokenizer
import torch
import pandas as pd

# Load the FAISS index
index = faiss.read_index('data/bug_report_index.faiss')

# Load the original data for reference
data = pd.read_pickle('data/bug_report_embeddings.pkl')

# Initialize the BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

def encode_text(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

def search_similar_bugs(query, top_k=5):
    query_vector = encode_text(query)
    distances, indices = index.search(query_vector, top_k)
    results = data.iloc[indices[0]]
    return results

# Example query
query = "example bug report text"
results = search_similar_bugs(query)

print("Top similar bug reports:")
print(results)
