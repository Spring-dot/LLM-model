# LLM Bug Report Analysis Tool

## Overview

This project provides a tool to analyze and retrieve similar bug reports using a Large Language Model (LLM) for embeddings and FAISS for efficient similarity search. The tool helps in quickly finding similar bug reports and their solutions, improving the efficiency of handling customer issues.

## Features

- **Bug Report Embedding**: Uses BERT to convert bug report text into embeddings.
- **Similarity Search**: Utilizes FAISS for fast and efficient similarity searches among bug reports.
- **Sample Dataset**: Generates a sample dataset of bug reports for demonstration purposes.

## Requirements

- Python 3.8+
- `pandas`
- `torch`
- `transformers`
- `faiss-cpu`
- `scikit-learn`

