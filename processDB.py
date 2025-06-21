
import sqlite3
import numpy as np
import requests
from parser import parse_snippets

print("⚠️ Loading embedding model... (this might take a minute)")
from sentence_transformers import SentenceTransformer

embeddingModel = SentenceTransformer("all-MiniLM-L6-v2")

DB_PATH = 'docs.db' # Your database file
db = sqlite3.connect(DB_PATH)
cursor = db.cursor()


with open(".docs", "r") as file:
    libraries = file.read().splitlines()

for libraryReference in libraries:
    library = libraryReference.split("/")[1]
    print(f"Processing {library}...")
    print(f"\t🛜 Downloading llms.txt...")
       
    url = f"https://context7.com/{libraryReference}/llms.txt?tokens=10000000"
    docs = requests.get(url).text
    
    print("\t🛠️ Parsing response...")
    parsed = parse_snippets(docs)
    
    docsInsert = []
    snippetsInsert = []

    for doc in parsed:
        docsInsert.append((doc["description"], doc["title"], doc["source"]))
        for snippet in doc["snippets"]:
            snippetsInsert.append((doc["title"], snippet["code"], snippet["language"]))
    
    
    print("\t💾 Adding to database...")

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {library}docs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        title TEXT NOT NULL,
        link TEXT
    )
    """)

    cursor.executemany(f"""
        INSERT INTO {library}docs (text, title, link)
        VALUES (?, ?, ?)
    """, docsInsert)

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {library}snippets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        code TEXT NOT NULL,
        language TEXT
    )
    """)
    
    cursor.executemany(f"""
    INSERT INTO {library}snippets (title,code, language)
    VALUES (?, ?, ?)
    """, snippetsInsert)

    print("\t🤖 Generating embeddings...")

    titles = cursor.execute(f"select title from {library}docs").fetchall()
    titles = [title[0] for title in titles]

    embeddings = embeddingModel.encode(titles)
    np.save(f"embeddings/{library}.npy", embeddings)

    print("\t✅ Done!")
    db.commit()