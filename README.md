# web-scraping

This project contains Python scripts for scraping book data from the website [Books to Scrape](https://books.toscrape.com/).

## Features

- **Command-line Script (`main.py`)**:
  - Fetches book data such as title, price, and availability from all pages of the website.
  - Optionally divides the scraped book data into separate CSV files based on genre.
  - Saves the scraped data into a `data` folder.

- **Flask Web Application (`app.py`)**:
  - Allows users to scrape books by category through a web interface.
  - Users can specify the category and the number of pages to scrape.
  - Downloads the scraped data as a CSV file.

## How to Use

### Command-line Script (`main.py`)

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. When prompted, choose whether to divide books by genre:
   - If you select "yes", the script will create separate CSV files for each genre in the `data` folder.
   - If you select "no", the script will save all books into a single file named `books.csv` in the `data` folder.

### Flask Web Application (`app.py`)

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to `http://127.0.0.1:5000`.

4. Select a category and the number of pages to scrape, then click "Submit" to download the scraped data as a CSV file.

## File Overview

- `main.py`: Command-line script for scraping and saving book data.
- `app.py`: Flask web application for scraping books by category.
- `templates/index.html`: HTML template for the Flask web interface.
- `data/`: Folder where the scraped CSV files are saved (used by `main.py`).
- `requirements.txt`: Lists the Python dependencies for the project.