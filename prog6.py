from transformers import pipeline

print("Loading sentiment analysis model...")
senti_analyse = pipeline('sentiment-analysis')

def analyse_sentiment(text):
  result = senti_analyse(text)[0]
  label = result['label']
  score = result['score']
  print(f"\nInput Text: {text}")
  print(f"Label:{label} (Confidence: {score:.4f})")
  return result

customer_reviews = [
   f"I love this product, its amazing.",
    f"I am so disappointed in this product.",
    f"This product is mediocre.",
    f"I feel I wasted my money on this useless product.",
    f"I am so happy that I purchased it."
]
for review in customer_reviews:
  analyse_sentiment(review)
