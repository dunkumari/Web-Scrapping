import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "http://books.toscrape.com/"

# Make a request to the website
response = requests.get(url)
response.raise_for_status()  # Checking the  request was successful

# Parse the content of the request with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting data
books = []
for article in soup.find_all('article', class_='product_pod'):
    title = article.h3.a['title']
    price = article.find('p', class_='price_color').text
    availability = article.find('p', class_='instock availability').text.strip()
    books.append({
        'Title': title,
        'Price': price,
        'Availability': availability
    })

# Convert to DataFrame
df = pd.DataFrame(books)

# Save to CSV
df.to_csv('books.csv', index=False)

print("Data has been scraped and saved to books.csv")
