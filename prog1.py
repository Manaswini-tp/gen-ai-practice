import numpy as np
import gensim.downloader as api

print("Loading pre-trained word vectors...")
word_vectors = api.load("word2vec-google-news-300")

def explore_word_relationships(w1,w2,w3):
  try:
    vec1 = word_vectors[w1]
    vec2 = word_vectors[w2]
    vec3 = word_vectors[w3]
    res = vec1-vec2+vec3
    sim_word = word_vectors.similar_by_vector(res, topn=5)
    input_words = {w1,w2,w3}
    filtered_words = [(w,sim) for w,sim in sim_word if w not in input_words]
    print(f"Words related to {w1}-{w2}+{w3}: ")
    for w,sim in filtered_words:
      print(f"{w}:{sim:.2f}")
  except KeyError as e:
    print(f"Error: {e} not found in vocabulary")

def similarities(w1,w2):
  try:
    sim = word_vectors.similarity(w1,w2)
    print(f"Similarity between {w1} and {w2}: {sim:.2f}% ")
  except KeyError as e:
    print(f"Error: {e} not found in vocabulary")

def most_similar_words(w):
  try:
    word_sim = word_vectors.most_similar(w, topn=3)
    print(f"Most similar words to {w}: ")
    for w,sim in word_sim:
      print(f"{w}:{sim:.2f}")
  except KeyError as e:
    print(f"Error: {e} not found in vocabulary")

explore_word_relationships("king","man","woman")
most_similar_words("Hello")
similarities("manga","anime")
