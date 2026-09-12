import time

from src.search import SemanticSearcher


searcher = SemanticSearcher("index_store")

queries = [
    "space exploration and planets",
    "machine learning algorithms",
    "programming websites",
    "climate change",
    "personal money management"
]

start = time.perf_counter()

for query in queries:
    searcher.search(query, k=5)

total = time.perf_counter() - start

average = total / len(queries)

print(f"Total search time: {total:.4f} seconds")
print(f"Average search latency: {average:.4f} seconds")