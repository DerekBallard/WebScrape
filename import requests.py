import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.goodreads.com/quotes"

# Send HTTP GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all quote blocks
    quotes = soup.find_all('div', class_='quote')
    
    # Print each quote and author
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f'"{text}" — {author}')
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
