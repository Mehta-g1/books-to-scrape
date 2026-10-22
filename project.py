import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

errors = []
def fetch_page(page_no):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url=f"https://books.toscrape.com/catalogue/page-{page_no}.html", headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        return page_no, soup
    except Exception as e:
        msg = f"Error in page {page_no}: {e}"
        errors.append(msg)
        print(msg)
        return page_no, None

def filter_book_section(soup):
    try:
        books_section = soup.find_all('article', class_='product_pod')
    except Exception as e:
        msg = f"Error: {e}"
        errors.append(msg)
        print(msg)
        return None
    return books_section

def get_one_book(book_html, book_no):
    try:
        book_name = book_html.find_all('a')[1].text
        star_rating = book_html.find('p').attrs['class'][1]
        price = book_html.find('p', class_='price_color').text.strip()
        in_stock = book_html.find('p', class_='instock availability').text.strip()

        # maping star rating and stocks
        star_rating = {
            'One':1,
            'Two':2,
            'Three':3,
            'Four':4,
            'Five':5
        }.get(star_rating)
        in_stock = True if in_stock == "In stock" else False

    except Exception as e:
        msg = f'Error at book no. {book_no} : {e}'
        errors.append(msg)
        print(msg)
    return [book_no, book_name, price, star_rating, in_stock]

i=0
df = df = pd.DataFrame(columns=['Serial No.', 'Book Name', 'Price', 'Rating', 'Stock'])

with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(fetch_page, range(1, 51))
    for page_no, soup in results:
        if not soup:
            continue
        books_sections = filter_book_section(soup)
        if not books_sections:
            continue
        print("-"*20,f'\nPage No. {page_no}\n',"-"*20,'\n')
        for book_html in books_sections:
            i+=1
            book_info_clear = get_one_book(book_html, i)
            if not book_info_clear:
                continue

            df.loc[len(df)] = book_info_clear

df.to_csv('books.csv', index=False, encoding='utf=8')
print(errors) 