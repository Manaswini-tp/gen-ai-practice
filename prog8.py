# !pip install cohere langchain langchain-community langchain-core

import cohere
import getpass
from google.colab import auth, drive
from langchain_community.llms import Cohere
from langchain_core.prompts import PromptTemplate

auth.authenticate_user()
drive.mount('/content/drive')

file_path = "/content/drive/My Drive/Teaching.txt"
try:
  with open(file_path, "r", encoding="utf-8") as file:
    text_content = file.read()
  print("File loaded successfully")
except Exception as e:
  print(f"Error loading file: ", str(e))

COHERE_API_KEY = getpass.getpass("Enter your API key: ")
co = cohere.Client(COHERE_API_KEY)

formatted_prompt = (f"""
You are an AI assistant who will help in formatting the document.
Document: 
{text_content}
Provide:
1. A concise summary
2. 3 key-takeaways
3. Sentiment analysis (Positive/Negative/Neutral)
""")
response = co.chat(
  model = "command-a-03-2025",
  message = formatted_prompt
)
print(response.text)
