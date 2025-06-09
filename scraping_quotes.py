import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.goodreads.com/quotes"

# Set headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Send HTTP GET request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quoteDetails')

    for i, quote in enumerate(quotes, start=1):
        quote_text_block = quote.find('div', class_='quoteText')
        if quote_text_block:
            # Extract text and split to get author
            text_parts = quote_text_block.get_text(strip=True, separator=" ").split("―")
            if len(text_parts) == 2:
                quote_text = text_parts[0].strip().strip('“”"')
                author = text_parts[1].strip()
                print(f"{i}. \"{quote_text}\"\n   — {author}\n")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
