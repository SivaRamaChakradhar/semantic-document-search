import json
import time
from pathlib import Path
import numpy as np

from src.ingest import ingest_documents
from src.embed import DocumentEmbedder


def build_index(data_dir: str, output_dir: str):

    start_total = time.perf_counter()

    # -----------------------------
    # 1. Ingest documents
    # -----------------------------
    ingest_start = time.perf_counter()

    documents = ingest_documents(data_dir)

    ingest_time = time.perf_counter() - ingest_start

    if not documents:
        raise ValueError("No valid .txt documents found.")

    print(f"\nDocuments ingested: {len(documents)}")
    print(f"Ingestion time: {ingest_time:.4f} seconds")

    # -----------------------------
    # 2. Extract text
    # -----------------------------
    texts = [doc["content"] for doc in documents]

    # -----------------------------
    # 3. Generate embeddings
    # -----------------------------
    embedding_start = time.perf_counter()

    embedder = DocumentEmbedder()
    embeddings = embedder.generate_embeddings(texts)

    embedding_time = time.perf_counter() - embedding_start

    print(f"Embedding shape: {embeddings.shape}")
    print(f"Embedding time: {embedding_time:.4f} seconds")

    # -----------------------------
    # 4. Create metadata
    # -----------------------------
    metadata = []

    for doc in documents:

        snippet = " ".join(doc["content"].split())[:200]

        metadata.append({
            "id": doc["id"],
            "snippet": snippet
        })

    # -----------------------------
    # 5. Save index
    # -----------------------------
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    save_start = time.perf_counter()

    np.save(
        output_path / "embeddings.npy",
        embeddings
    )

    with open(
        output_path / "metadata.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            metadata,
            file,
            indent=2,
            ensure_ascii=False
        )

    save_time = time.perf_counter() - save_start
    total_time = time.perf_counter() - start_total

    print(f"Save time: {save_time:.4f} seconds")
    print(f"Total indexing time: {total_time:.4f} seconds")

    print("\nIndex successfully created!")
    print(f"Embeddings: {output_path / 'embeddings.npy'}")
    print(f"Metadata:   {output_path / 'metadata.json'}")