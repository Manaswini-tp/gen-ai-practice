from transformers import pipeline

print("Loading summarizing model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summary_text(text, max_length=None, min_length=None):
  if not max_length:
    max_length=min(len(text)//3, 150)
  if not min_length:
    min_length=max(30, max_length//3)
  sum_1 = summarizer(text, max_length=150, min_length=30, do_sample=False)
  sum_2 = summarizer(text, max_length=150, min_length=30, do_sample=True, temperature=0.95)
  sum_3 = summarizer(text, max_length=150, min_length=30, do_sample=False, num_beams=5)
  sum_4 = summarizer(text, max_length=150, min_length=30, do_sample=True, top_k=5,top_p=0.95)
  print("Original Text: \n")
  print(text)
  print("\nSummaries: \n")
  print("Default: ", sum_1[0]['summary_text'])
  print("Highly randomised: ", sum_2[0]['summary_text'])
  print("Conservative: ", sum_3[0]['summary_text'])
  print("Diverse: ", sum_4[0]['summary_text'])

long_text = """
The Mariana Trench remains one of the most hostile yet fascinating frontiers on Earth, plunging nearly 
eleven kilometers into the crust where the water pressure reaches an crushing eight tons per square inch. 
Despite these cataclysmic conditions, recent robotic expeditions have uncovered thriving ecosystems powered 
not by sunlight, but by chemosynthesis around hydrothermal vents. Microbes metabolize toxic sulfur compounds, 
forming the base of a bizarre food web that includes ghostly snailfish, giant amphipods, and massive single-celled 
xenophyophores. Marine biologists believe studying these extremophiles could unlock secrets regarding the origins 
of life on early Earth and guide astrobiologists in their search for organisms on icy moons like Europa. However, 
funding remains scarce as aerospace ventures consistently overshadow deep-ocean exploration, leaving over eighty 
percent of our own seabed entirely unmapped and misunderstood.
"""
summary_text(long_text)
  
