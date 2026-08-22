import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    # Target URL (a practice site designed for web scraping)
    url = "http://quotes.toscrape.com"

    # Send HTTP GET requests to the site
    response = requests.get(url)

    # Check if the requests was succesful (200 = OK)
    if response.status_code == 200:
        #Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        print("--- Data succesfully scraped! ---")
        for index, quote in enumerate(quotes, start=1):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            print(f"{index}. {text} - {author}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_quotes()