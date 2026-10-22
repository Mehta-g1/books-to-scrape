# Books to Scrape

A small Python web-scraping project that collects book information from [Books to Scrape](https://books.toscrape.com), a site intended for practicing web scraping.

The script visits all 50 catalogue pages and extracts each book's title, price, star rating, and stock status. It uses a thread pool to fetch pages concurrently and writes the collected data to `books.csv`.

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

The script prints page progress and any collected errors. The output file, `books.csv`, is created in the current working directory.
