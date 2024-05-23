import pandas as pd
from transformers import BertModel, BertTokenizer
import torch

# Load your data
data = pd.read_csv('data/bug_reports.csv')

# Initialize the BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

def encode_text(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

# Encode bug reports
data['embeddings'] = data['bug_report'].apply(encode_text)

# Save embeddings
data.to_pickle('data/bug_report_embeddings.pkl')
