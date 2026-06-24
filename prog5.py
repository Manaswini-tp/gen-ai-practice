import nltk
import random
import gensim.downloader as api

nltk.download('punkt')
print("Loading word vectors...")
wv = api.load("glove-wiki-gigaword-100")
print("loaded successfully!")

def get_sim_word(word):
  try:
    return [w[0] for w in wv.most_similar(word, topn=5)]
  except:
    print("Word not found")
    return []

def generate_paragraph(seed):
  sim = get_sim_word(seed)
  if len(sim)<5:
    print("Try other word..")
    return []
  sentences = [
    f"The {seed} is surrounded by {sim[0]} and {sim[1]}",
    f"The story of {seed} is incomplete without {sim[2]} and {sim[3]}",
    f"People often assosciate {seed} with {sim[4]}"
  ]
  return " ".join(random.choice(sentences) for _ in range(4))

seed = input("Enter seed word: ")
print("Generated paragraph: \n")
print(generate_paragraph(seed))
