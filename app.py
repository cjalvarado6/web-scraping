from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from io import BytesIO

app = Flask(__name__)

BASE_URL = "http://books.toscrape.com/catalogue/category/books/"
CATEGORY_URLS = {
    "Science": "science_22/index.html",
    "Travel": "travel_2/index.html",
    "Mystery": "mystery_3/index.html",
    "Historical Fiction": "historical-fiction_4/index.html"
}


def scrape_books(category, max_pages=1):
    if category not in CATEGORY_URLS:
        return pd.DataFrame()

    books = []
    page_url = BASE_URL + CATEGORY_URLS[category]
    base_path = page_url.rsplit('/', 1)[0]
    page_number = 1

    while page_number <= max_pages:
        res = requests.get(page_url)
        soup = BeautifulSoup(res.content, 'html.parser')

        for article in soup.select('article.product_pod'):
            title = article.h3.a['title']
            price = article.select_one('.price_color').text.strip()
            availability = article.select_one('.availability').text.strip()

            books.append({
                'Title': title,
                'Price': price,
                'Availability': availability
            })

        next_button = soup.select_one('li.next a')
        if next_button:
            page_url = f"{base_path}/{next_button['href']}"
        else:
            break

        page_number += 1

    return pd.DataFrame(books)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        pages = int(request.form['pages'])
        df = scrape_books(category, pages)

        output = BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)

        return send_file(
            output,
            download_name=f"{category}_books.csv",
            as_attachment=True,
            mimetype='text/csv'
        )

    return render_template('index.html', categories=CATEGORY_URLS.keys())


if __name__ == '__main__':
    app.run(debug=True)
