import streamlit as st
from sentence_transformers import SentenceTransformer
from vector_db import VectorDB

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize DB
db = VectorDB()

# Sample resumes
resumes = [
    {"name": "Resume1", "text": "Python developer with machine learning and AI experience"},
    {"name": "Resume2", "text": "Java backend developer with Spring Boot"},
    {"name": "Resume3", "text": "Frontend developer with React and JavaScript"},
]

# Insert into DB
for r in resumes:
    emb = model.encode(r["text"])
    db.insert(r["name"], r["text"], emb)

# UI
st.title("🔍 AI Resume Search (Endee Inspired)")
st.write("Using vector database concepts from Endee")

query = st.text_input("Enter your query:")

if st.button("Search"):
    if query:
        q_emb = model.encode(query)
        results = db.search(q_emb)

        st.subheader("Results:")
        for name, text, score in results:
            st.write(f"**{name}**")
            st.write(text)
            st.write(f"Score: {score:.2f}")
            st.write("---")
    else:
        st.warning("Please enter a query")