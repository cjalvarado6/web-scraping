import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://books.toscrape.com/"

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def scrape_books(soup):
    books = []
    for book in soup.select('.product_pod'):
        title = book.h3.a['title']
        price = book.select_one('.price_color').text
        availability = book.select_one('.availability').text.strip()
        books.append({'title': title, 'price': price, 'availability': availability})
    return books

def scrape_all_pages():
    url = BASE_URL + "catalogue/page-1.html"
    all_books = []
    while url:
        soup = fetch_page(url)
        all_books.extend(scrape_books(soup))
        next_page = soup.select_one('.next a')
        url = BASE_URL + "catalogue/" + next_page['href'] if next_page else None
    return all_books

def save_to_csv(books, filename="books.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price', 'availability'])
        writer.writeheader()
        writer.writerows(books)

if __name__ == "__main__":
    print("Scraping books...")
    books = scrape_all_pages()
    save_to_csv(books)
    print(f"Scraped {len(books)} books and saved to 'books.csv'.")
