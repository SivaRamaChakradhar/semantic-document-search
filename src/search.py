import json
from pathlib import Path
from typing import List, Dict, Any

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from src.embed import DocumentEmbedder


class SemanticSearcher:

    def __init__(self, index_dir: str):

        index_path = Path(index_dir)

        embeddings_path = index_path / "embeddings.npy"
        metadata_path = index_path / "metadata.json"

        if not embeddings_path.exists():
            raise FileNotFoundError(
                f"Missing embeddings file: {embeddings_path}"
            )

        if not metadata_path.exists():
            raise FileNotFoundError(
                f"Missing metadata file: {metadata_path}"
            )

        # Load index only once
        self.embeddings = np.load(embeddings_path)

        with open(
            metadata_path,
            "r",
            encoding="utf-8"
        ) as file:
            self.metadata = json.load(file)

        if len(self.embeddings) != len(self.metadata):
            raise ValueError(
                "Embeddings and metadata are not aligned."
            )

        # Load model once
        self.embedder = DocumentEmbedder()

    def search(
        self,
        query: str,
        k: int = 5
    ) -> List[Dict[str, Any]]:

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        if k <= 0:
            raise ValueError("k must be a positive integer.")

        # Embed query
        query_vector = self.embedder.generate_embeddings(
            [query]
        )

        # Calculate cosine similarity
        scores = cosine_similarity(
            query_vector,
            self.embeddings
        )[0]

        # Sort descending
        ranked_indices = np.argsort(scores)[::-1]

        # Return at most k results
        ranked_indices = ranked_indices[:k]

        results = []

        for index in ranked_indices:

            results.append({
                "id": self.metadata[index]["id"],
                "score": round(float(scores[index]), 4),
                "snippet": self.metadata[index]["snippet"]
            })

        return results