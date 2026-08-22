import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_and_save():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_elements = soup.find_all('div', class_='quote')
    
    data_list = []
    
    for idx, quote_el in enumerate(quotes_elements, start=1):
        text = quote_el.find('span', class_='text').text.strip("“”")
        author = quote_el.find('small', class_='author').text.strip()
        tags = [tag.text for tag in quote_el.find_all('a', class_='tag')]
        
        data_list.append({
            "id": idx,
            "quote": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    # 1. Save to CSV
    csv_file = "quotes.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(data_list)
    print(f"Data successfully exported to {csv_file}")

    # 2. Save to JSON
    json_file = "quotes.json"
    with open(json_file, mode="w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4, ensure_ascii=False)
    print(f"Data successfully exported to {json_file}")

if __name__ == "__main__":
    scrape_and_save()