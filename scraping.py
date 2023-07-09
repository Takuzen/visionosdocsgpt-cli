import os
import csv
import openai
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
assert OPENAI_API_KEY, "OPENAI_API_KEY environment variable is missing from .env"
openai.api_key = OPENAI_API_KEY

# Load the HTML file
with open('./lp.text', 'r') as file:
    html_code = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Find all <p> and <h> tags
paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4'])

# Make text string for OpenAI text embedding API
text = ""
for tag in paragraphs:
    text += tag.text + "\n"
print(text)

# Get embedding by OpenAI text embedding API.
# See https://platform.openai.com/docs/guides/embeddings/what-are-embeddings
response = openai.Embedding.create(
    input=text,
    model="text-embedding-ada-002"
)
embedding = response['data'][0]['embedding']
print(embedding)

# Open the CSV file for writing
with open('visionos_docs_2023_07_09.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write column names to the CSV file
    writer.writerow(['text', 'embedding'])
    
    # Write text and embedding vector to the CSV file
    writer.writerow([text,",".join(map(str, embedding))])