# Semantic Document Search Engine

## Overview

This project implements a command-line semantic document search engine
using Sentence-Transformers.

Unlike traditional keyword search, the system converts documents and
queries into vector embeddings and compares them using cosine similarity.

## Architecture

Documents
    ↓
Data Ingestion
    ↓
Sentence Transformer
    ↓
Vector Embeddings
    ↓
NumPy Index
    ↓
Cosine Similarity
    ↓
Top-K Results

## Technologies

- Python
- Sentence-Transformers
- all-MiniLM-L6-v2
- NumPy
- Scikit-learn

### Search Benchmark

The search benchmark was executed after the Sentence-Transformer model
was loaded, so model initialization time is excluded from query latency.

| Metric                 | Result |
| Number of queries      | 5      |
| Total search time      | 0.9472 seconds |
| Average search latency | 0.1894 seconds |

## Project Structure

```text
data/
index_store/
src/
    ingest.py
    embed.py
    indexer.py
    search.py
cli.py
requirements.txt
README.md
