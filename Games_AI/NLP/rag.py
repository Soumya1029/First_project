import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample documents (Could be a knowledge base)
documents = [
    "LLMs are used in AI-powered chatbots.",
    "They improve machine translation quality.",
    "LLMs assist in code generation and text summarization.",
    "They enhance speech recognition and conversational AI."
]

# Convert documents to vectors
doc_vectors = np.array([model.encode(doc) for doc in documents])

# Create FAISS index
index = faiss.IndexFlatL2(doc_vectors.shape[1])
index.add(doc_vectors)

def search(query):
    """Retrieves the most relevant document for a given query"""
    query_vector = np.array([model.encode(query)])
    D, I = index.search(query_vector, 1)
    return documents[I[0][0]]

# Example usage
query = "How are LLMs used in chatbots?"
print(f"Query: {query}")
print(f"Best Match: {search(query)}")
