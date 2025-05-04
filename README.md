# web-scraping

This project contains a Python script (`main.py`) for scraping book data from the website [Books to Scrape](https://books.toscrape.com/).

## Features

- Fetches book data such as title, price, and availability from all pages of the website.
- Saves the scraped data into a CSV file (`books.csv`).

## How to Use

1. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. The script will scrape all the books and save the data into a file named `books.csv` in the current directory.

## File Overview

- `main.py`: Contains the logic for fetching, scraping, and saving book data.