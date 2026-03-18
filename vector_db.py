import numpy as np

class VectorDB:
    def __init__(self):
        self.data = []

    def insert(self, name, text, embedding):
        self.data.append({
            "name": name,
            "text": text,
            "embedding": embedding
        })

    def search(self, query_embedding, top_k=3):
        results = []

        for item in self.data:
            score = np.dot(query_embedding, item["embedding"]) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(item["embedding"])
            )
            results.append((item["name"], item["text"], score))

        results.sort(key=lambda x: x[2], reverse=True)
        return results[:top_k]