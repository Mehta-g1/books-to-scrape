# Books to Scrape

A Python web-scraping project that gathers book information from [Books to Scrape](https://books.toscrape.com), a website created for practicing web scraping.

## Task and objective

The task is to build a program that retrieves multiple web pages, parses their HTML, extracts product information, and saves the results in a CSV file for further analysis. This project uses the Books to Scrape catalogue, which contains 1,000 books across 50 pages.

For each book, the program collects:

- Title
- Price
- Star rating, represented as a number from 1 to 5
- Availability, represented as `True` or `False`

## How it works

The `project.py` script:

1. Fetches catalogue pages 1 through 50 with `requests`.
2. Uses a thread pool to retrieve multiple pages concurrently.
3. Parses each page with BeautifulSoup and finds the book listings.
4. Extracts the title, price, rating, and availability for each listing.
5. Stores the results in a pandas DataFrame and exports them to `books.csv`.
6. Prints page progress and any errors encountered during scraping.

The CSV contains these columns: `Serial No.`, `Book Name`, `Price`, `Rating`, and `Stock`.

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`
- `pandas`

Install the dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

## Run

From the project directory, run:

```bash
python project.py
```

The script creates or overwrites `books.csv` in the current working directory. It requires an internet connection to retrieve the catalogue pages.
