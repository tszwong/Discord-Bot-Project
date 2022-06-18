# created by: Tsz Kit Wong
# webScrap.py

from bs4 import BeautifulSoup
import requests
import urllib.parse
import random


# info that will be displayed to user
price_info = {}
display = ""

# function that does all the scraping
def find_price(soup, ticker):
    global price_info
    # searches for the specific tag containing key price information
    results = soup.find("div", class_="intraday__data")
    main_line = results.find_all("bg-quote")

    # refining and stripping down the contents to the number values
    price_info[ticker] = {}

    # add open or closed market status to info section

    price_info[ticker]["Current Price"] = "$" + main_line[0].text.strip()
    price_info[ticker]["Change ($)"] = main_line[2].text.strip()
    price_info[ticker]["Change (%)"] = main_line[3].text.strip()


# helper function that creates a dynamic link for scraping
def process_link(ticker):
    # link creation
    random_num = random.randint(0,100000)
    link = ""

    link = f"https://www.marketwatch.com/investing/stock/{ticker}?mod=search_symbol" \
            f"?{random_num}"

    link_txt = urllib.parse.quote(link, safe="%:/?=&*+")

    # getting the html file contents
    page = requests.get(link_txt)
    soup = BeautifulSoup(page.content, "html.parser")
    page.close()
    return soup


# helper function that prints out info in a clear and readable way
def display_price_info(item):
    global display
    for key, value in item.items():
        display += f"\nStock: {key.upper()}\n"
        for info in value:
            display += f"{info}: {value[info]}\n"


def initiate(ticker):
    global display
    global price_info
    try:
        # initiates scraping
        soup = process_link(ticker)
        find_price(soup, ticker)
        display_price_info(price_info)
        price_info.clear()
        new_str = ""
        new_str, display = display, new_str

        return new_str

    except AttributeError:  # incase the ticker does not exist
        return ("Invalid Ticker: item does not exist")
