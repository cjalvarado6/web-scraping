import requests
from bs4 import BeautifulSoup
import csv
import os

BASE_URL = "https://books.toscrape.com/"

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def scrape_books(soup):
    books = []
    for book in soup.select('.product_pod'):
        title = book.h3.a['title']
        price = book.select_one('.price_color').text
        availability = book.select_one('.availability').text.strip()
        books.append({'title': title, 'price': price, 'availability': availability})
    return books

def scrape_genres(soup):
    genres = {}
    for category in soup.select('.side_categories ul li ul li a'):
        genre_name = category.text.strip()
        genre_url = BASE_URL + category['href']
        genres[genre_name] = genre_url
    return genres

def scrape_paginated_data(start_url, scrape_function):
    data = []
    url = start_url
    while url:
        soup = fetch_page(url)
        if not soup:
            break
        data.extend(scrape_function(soup))
        next_page = soup.select_one('.next a')
        url = BASE_URL + "catalogue/" + next_page['href'] if next_page else None
    return data

def save_to_csv(data, filepath):
    try:
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'price', 'availability'])
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        print(f"Error saving file {filepath}: {e}")

def save_books_by_genre(genre_books):
    for genre, books in genre_books.items():
        filename = f"data/{genre.replace(' ', '_').lower()}.csv"
        save_to_csv(books, filename)

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    print("Scraping books...")
    divide_by_genre = input("Do you want to divide books by genre? (yes/no): ").strip().lower() == "yes"
    if divide_by_genre:
        soup = fetch_page(BASE_URL)
        if soup:
            genres = scrape_genres(soup)
            genre_books = {genre: scrape_paginated_data(url, scrape_books) for genre, url in genres.items()}
            save_books_by_genre(genre_books)
            print(f"Scraped books by genre and saved to 'data/' folder.")
    else:
        books = scrape_paginated_data(BASE_URL + "catalogue/page-1.html", scrape_books)
        save_to_csv(books, "data/books.csv")
        print(f"Scraped {len(books)} books and saved to 'data/books.csv'.")
