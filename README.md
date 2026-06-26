# Generative AI & NLP Lab Programs

This repository contains Python implementations of various experiments related to **Word Embeddings, Generative AI, Hugging Face Models, LangChain, and NLP applications**.

The programs were developed and executed as part of the Generative AI / NLP laboratory exercises.

---

## Technologies Used

- Python
- Gensim
- Word2Vec / GloVe Embeddings
- Transformers (Hugging Face)
- GPT-2
- NLTK
- Scikit-learn
- Matplotlib
- LangChain
- Cohere API
- Wikipedia API
- Pydantic

---

## Programs Included

### 1. Word Vector Exploration & Vector Arithmetic

- Loaded pre-trained word embeddings
- Explored relationships between words using vector arithmetic


Analyzed semantic relationships captured by word vectors.

---

### 2. Word Embedding Visualization & Similarity Search

- Applied dimensionality reduction techniques:
  - PCA
  - t-SNE

- Visualized word embeddings in 2D space

- Selected domain-specific words and analyzed clusters

- Generated semantically similar words for a given input


### 3. Custom Word2Vec Model Training

- Trained a Word2Vec model on a custom dataset

- Generated domain-specific embeddings

- Analyzed how the model captures relationships between words


---

### 4. Prompt Enhancement Using Word Embeddings

- Retrieved similar words using embeddings

- Used similar words to enrich Generative AI prompts

Workflow:

```
Input Prompt
      |
      ↓
Find Similar Words
      |
      ↓
Create Enriched Prompt
      |
      ↓
Generate AI Response
      |
      ↓
Compare Results
```

Used GPT-2 for response generation.

---

### 5. Creative Text Generation Using Embeddings

- Took a seed word as input

- Retrieved semantically similar words

- Used generated words to create a short creative paragraph

Example:

Seed word:
```
ocean
```

Generated related words:
```
waves, sea, blue, water...
```

---

### 6. Sentiment Analysis Using Hugging Face

- Used a pre-trained Hugging Face sentiment analysis pipeline

- Classified text into:

```
Positive
Negative
```

Example applications:
- Review analysis
- Feedback classification

---

### 7. Text Summarization Using Hugging Face

- Used a pre-trained summarization model

- Converted long passages into concise summaries

Workflow:

```
Long Text
    ↓
Summarization Model
    ↓
Short Summary
```

---

### 8. LangChain + Cohere Prompt Template

- Installed and used:

  - LangChain
  - Cohere
  - LangChain Community

- Integrated Cohere API

- Created prompt templates

- Generated formatted responses using LLMs

---

### 9. Institution Information Extraction Using Wikipedia + Pydantic

- Took institution name as input

- Retrieved information from Wikipedia

- Used Pydantic schema for structured output

Extracted:

- Founder
- Founded year
- Branches
- Number of employees
- Institution summary

---

### 10. Indian Penal Code Chatbot

Created a chatbot based on Indian Penal Code information.

Features:

- Retrieved IPC content from Wikipedia
- Used Cohere API for response generation
- Answered user queries related to IPC sections

Example:

```
User:
Explain Section 180

Bot:
Provides IPC-related explanation
```

---

#Venv

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## Running Programs

Execute any program using:

```bash
python filename.py
```

---

## API Requirements

Some programs require API access:

- Cohere API Key

Set your key when prompted.

---
