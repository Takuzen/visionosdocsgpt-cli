from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('./lp.text', 'r') as file:
    html_code = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Find all <p> and <h> tags
paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4'])

# Open the CSV file for writing
with open('visionos_docs_2023_07_09.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)
    
    # Loop through the extracted tags and process them
    for tag in paragraphs:
        # Write the tag text to the CSV file
        writer.writerow([tag.text])