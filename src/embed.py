from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List


class DocumentEmbedder:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2"
    ):
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(
        self,
        texts: List[str]
    ) -> np.ndarray:

        if not texts:
            return np.empty((0, 384), dtype=np.float32)

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True
        )

        return np.asarray(embeddings, dtype=np.float32)