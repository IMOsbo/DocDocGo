from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search
from flask import Flask, request, render_template
import numpy as np

import sqlite3
from collections import defaultdict
from functools import lru_cache

app = Flask(__name__)

embeddingModel = SentenceTransformer("all-MiniLM-L6-v2")

DB_PATH = 'docs.db'

@lru_cache(maxsize=10)
def loadEmbeddings(library):
    embeddings = np.load("embeddings/pandas.npy")
    return embeddings

def getDocs(library, matches):
    with sqlite3.connect(DB_PATH) as db:
        cursor = db.cursor()

        placeholder = ','.join(['?'] * len(matches))
        documents = cursor.execute(f"select * from {library}docs where id in ({placeholder})", matches).fetchall()
    
        titles = [match[2] for match in documents]
        placeholder = ','.join(['?'] * len(titles))
        snippets = cursor.execute(f"select * from {library}snippets where title in ({placeholder})", titles).fetchall()
        

        snippets_by_title = defaultdict(list)
        for _, title, code, language in snippets:
            snippets_by_title[title].append({"code": code, "language": language})

    results = []
    for _, description, title, link in documents:
        results.append({
            "title": title,
            "description": description,
            "source": link,
            "snippets": snippets_by_title[title]
        })
    return results
    

@app.route('/search')
def search():
    query = request.args.get('query')
    numHits = int(request.args.get('hits'))
    library = request.args.get('library')
    newEmbedding = embeddingModel.encode([query])

    embeddings = loadEmbeddings(library)

    hits = semantic_search(newEmbedding, embeddings, top_k=numHits)
    relevantChunks = [hit['corpus_id']+1 for hit in hits[0]]

    docs = getDocs(library, relevantChunks)
    
    return render_template('code.html', results=docs)

@app.route("/")
def root():
    with open(".docs", "r") as file:
        libraries = file.read().splitlines()
        libraries = [library.split("/")[1] for library in libraries]
    return render_template("search.html", libraries=libraries)

if __name__ == "__main__":
    app.run(debug=True)
