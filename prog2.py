import numpy as np
import matplotlib.pyplot as plt
import gensim.downloader as api
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

print("Loading pre-trained word vector model...")
word_vectors = api.load("word2vec-google-news-300")

def explore_word_relationship(word1, word2, word3):
  vec1 = word_vectors[word1]
  vec2 = word_vectors[word2]
  vec3 = word_vectors[word3]
  result = vec1-vec2+vec3
  sim_words = word_vectors.similar_by_vector(result, topn=10)
  count=1
  for w, sim in sim_words:
    print(f"{w}: {sim:.4f}")
    if count==6:
      break
  return [w for w, _ in sim_words]

def visualise(words, method='pca'):
  vectors = np.array([word_vectors[word] for word in words])
  if method=='pca':
    reduced = PCA(n_components=2).fit_transform(vectors)
  else:
    reduced = TSNE(n_components=2, random_state=42, perplexity=3).fit_transform(vectors)
  plt.figure(figsize=(10,6))
  for i, word in enumerate(words):
    plt.scatter(reduced[i,0], reduced[i,1])
    plt.text(reduced[i,0], reduced[i,1], word)
  plt.title(f"Word Embeddings Visualisation using {method}")
  plt.grid()
  plt.show()

base_words = ["king", "man", "woman"]
extra_words = explore_word_relationship("king", "man", "woman")
all_words = base_words+extra_words
visualise(all_words, 'pca')
visualise(all_words, 'tsne')

def generate_similar_words(word):
  try:
    sim_words = word_vectors(word, topn=5)
    for w, sim in sim_words:
      print(f"{w}: {sim:.4f}")
  except Keyerror:
    print("Word not found")

domain_words = ["computer", "software", "hardware", "programming", "data", "analytics", "machine", "learning", "networking", "AI"]
generate_similar_words("computer")
generate_similar_words("learning")

visualise(domain_words, 'pca')
visualise(domain_words, 'tsne')

  
