# web-scraping

This project contains a Python script (`main.py`) for scraping book data from the website [Books to Scrape](https://books.toscrape.com/).

## Features

- Fetches book data such as title, price, and availability from all pages of the website.
- Optionally divides the scraped book data into separate CSV files based on genre.
- Saves the scraped data into a `data` folder.

## How to Use

1. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. When prompted, choose whether to divide books by genre:
   - If you select "yes", the script will create separate CSV files for each genre in the `data` folder.
   - If you select "no", the script will save all books into a single file named `books.csv` in the `data` folder.

## File Overview

- `main.py`: Contains the logic for fetching, scraping, and saving book data.
- `data/`: Folder where the scraped CSV files are saved.