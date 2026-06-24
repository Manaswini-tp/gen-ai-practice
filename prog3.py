import numpy as np
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE

medical_corpus = [
  "The patient was diagnosed with diabetes and hypertension.",
    "MRI scans reveal abnormalities in the brain tissue.",
    "The treatment involves antibiotics and regular monitoring.",
    "Symptoms include fever fatigue and muscle pain.",
    "The vaccine is effective against several viral infections.",
    "Doctors recommend physical therapy for recovery.",
    "The clinical trial results were published in the journal.",
    "The surgeon performed a minimally invasive procedure.",
    "The prescription includes pain relievers and anti inflammatory drugs.",
    "The diagnosis confirmed a rare genetic disorder."
]

processed_corpus = [sentence.lower().split() for sentence in medical_corpus]

print("Training Word2Vec model...")
model = Word2Vec(sentences=processed_corpus, vector_size=100, min_count=1, workers=4, epochs=50)
print("Training ended!!!")

words = list(model.wv.index_to_key)
embeddings = np.array([model.wv[w] for w in words)
tsne = TSNE(n_components=2, random_state=42, perplexity=5, max_iter=300)
tsne_result = tsne.fit_transform(embeddings)

plt.figure(figsize=(10,8))
for i, word in enumerate(words):
  plt.scatter(tsne_result[i,0], tsne_result[i,1])
  plt.text(tsne_result[i,0]+0.02, tsne_result[i,1]+0.02, word)
plt.title("Word Embeddings Visualization (medical corpus)")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid()
plt.show()

def similar_words(word):
  try:
    print("Similar words for", word)
    sim_words = model.wv.most_similar(word, topn=5)
    for w, sim in sim_words:
      print(f"{w}: {sim:.4f}")
  except KeyError:
    print("Word not found")

similar_words("vaccine")
similar_words("corona")
