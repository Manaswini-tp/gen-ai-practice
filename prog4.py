import gensim.downloader as api
from transformers import pipeline
import nltk

nltk.download("punkt")

print("Loading word vectors...")
word_vectors = api.load("glove-wiki-gigaword-100")


print("Loading GPT-2 model...")
generator = pipeline(
    "text-generation",
    model="gpt2"
)


# Original prompt
original_prompt = "Who is king."

print("\nOriginal Prompt:")
print(original_prompt)


# Find semantically similar word
similar_word = word_vectors.most_similar(
    "king",
    topn=1
)[0][0]


print("\nReplacing 'king' with:", similar_word)


# Create enriched prompt
enriched_prompt = original_prompt.replace(
    "king",
    similar_word
)


print("\nEnriched Prompt:")
print(enriched_prompt)



# Generate response function
def generate_response(prompt):

    result = generator(
        prompt,
        max_new_tokens=50,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]



# Generate outputs
print("\nGenerating original response...")

original_response = generate_response(
    original_prompt
)


print("\nGenerating enriched response...")

enriched_response = generate_response(
    enriched_prompt
)



# Display outputs
print("\nOriginal Response:")
print(original_response)


print("\nEnriched Response:")
print(enriched_response)



# Comparison
print("\nComparison:")

print(
    "Original Length:",
    len(original_response)
)

print(
    "Enriched Length:",
    len(enriched_response)
)

print(
    "Original Sentences:",
    original_response.count(".")
)

print(
    "Enriched Sentences:",
    enriched_response.count(".")
)
