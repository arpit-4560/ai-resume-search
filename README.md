🔍 AI Resume Search System (Endee Inspired)

📌 Overview
This project is an AI-powered resume search system that allows users to find the most relevant resumes using natural language queries.
It uses semantic search techniques to understand the meaning of the query instead of just matching keywords.
This project is inspired by the Endee repository and implements a custom vector database for semantic search.

🚀 Features
* Semantic search using AI embeddings
* Fast similarity-based resume retrieval
* Simple and interactive UI using Streamlit
* Real-world recruitment use case

🧠 System Design
1. Input query is given by the user
2. Query is converted into vector embedding
3. Resume data is also converted into embeddings
4. Cosine similarity is used to find the best match
5. Top results are displayed in UI

⚙️ Tech Stack
* Python
* Sentence Transformers
* Streamlit
* NumPy

🔗 Endee Integration

This project is inspired by the working principles of vector databases like Endee.
Due to the experimental nature of the Endee repository, direct pip-based integration is not used.
Instead, this project implements:
* Vector embeddings
* Similarity search
* Retrieval mechanism
These simulate how vector databases like Endee operate internally.

▶️ Run the Project

```bash
pip install sentence-transformers streamlit numpy
streamlit run app.py
```

📊 Example Queries
* python developer
* machine learning engineer
* frontend developer

📁 Project Structure
* app.py → Main application
* README.md → Documentation

🎯 Use Case
This system helps recruiters quickly find the best candidates based on skills and experience using AI.

📸 Output
The system displays ranked resumes based on similarity score.
<img width="638" height="741" alt="Screenshot 2026-03-18 152524" src="https://github.com/user-attachments/assets/b85ea4b6-a543-40d6-9422-7b68a33d105d" />


⭐ Note
Endee repository has been forked and referenced as part of this project submission.
