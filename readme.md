# DocDocGo 🦆 - 'documentation for out there'

![image](https://github.com/user-attachments/assets/4c7c7626-68bf-4ef4-b034-10b626dc20f7)

We've all been there. Trying to push through the final stretches of a project - and then the internet goes out. Your fancy Google searches? StackOverflow? (ChatGPT?) All gone.

You *can* download `zip` folders of docs from your favorite libraries, but searching those websites are... often lacking. To fix this, I leveraged Context7's wonderfully structured docs - see an example here.

```
TITLE: Conditional New Column Creation with Multiple Conditions using `numpy.select`
DESCRIPTION: This snippet shows how to create a new column based on multiple, ordered conditions using `numpy.select()`. It defines a list of boolean conditions and corresponding choices, assigning a default value if none of the conditions are met. This is highly efficient for complex conditional logic.
SOURCE: https://github.com/pandas-dev/pandas/blob/main/doc/source/user_guide/indexing.rst#_snippet_87

LANGUAGE: python
CODE:
\`\`\`
conditions = [
    (df['col2'] == 'Z') & (df['col1'] == 'A'),
    (df['col2'] == 'Z') & (df['col1'] == 'B'),
    (df['col1'] == 'B')
]
choices = ['yellow', 'blue', 'purple']
df['color'] = np.select(conditions, choices, default='black')
df
\`\`\`
```

Context7 is clearly structured and meant for LLMs, but it also works pretty well for human documentation too...<https://context7.com/about> The clear structure makes it a great fit for embeddings search...

## Installation

```
git clone https://github.com/IMOsbo/DocDocGo
pip install requirements.txt
```

Once you've installed everything, add the docs you want to include to `.docs`. See the example `.docs` file for examples. 

![image](https://github.com/user-attachments/assets/3f2e13b7-fff5-4a64-9cf7-9dab001c8b23)


```
python processDB.py
```

Once you've finished downloading the docs and created the database, you can start the app!

```
python searchApp.py
```

## Tech Stack

I purposefully made this as minimal as possible - no massive dependencies here.

- Embeddings: handled with [Sentence Transformers](https://sbert.net/)
- Document storage: [sqlite](https://sqlite.org/)
- Server handling: [Flask](https://flask.palletsprojects.com/)
- Front end: [matcha.css](https://github.com/lowlighter/matcha) and [htmx](https://htmx.org/)
