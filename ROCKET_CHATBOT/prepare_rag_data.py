# prepare_rag_data.py
import sqlite3
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Connect to the correct database
conn = sqlite3.connect("space_data.db")
cursor = conn.cursor()

# Pull rocket + mission descriptions
cursor.execute("SELECT DISTINCT rocket, mission FROM missions WHERE mission IS NOT NULL")
rows = cursor.fetchall()
conn.close()

# Format documents
documents = [f"{rocket}: {mission}" for rocket, mission in rows if mission.strip()]
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(documents)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Save everything
with open("rag_documents.pkl", "wb") as f:
    pickle.dump(documents, f)
faiss.write_index(index, "rag_index.index")

print(f"✅ Indexed {len(documents)} missions for RAG.")
print("✅ RAG data preparation complete")