# IMPORTING THE REQUIRED MODULES TO SCRAPE REQUIRED DATA
import requests
from bs4 import BeautifulSoup


def get_script_detail(symbol):
    # this function returns the details of a certain company.
    res = requests.get('https://www.sharesansar.com/today-share-price')  # getting response from the website
    soup = BeautifulSoup(res.text, 'html.parser')  # changes the string from res.text to soup object using html parser
    stock_table = soup.tbody  # getting the table containing stock details
    tag = stock_table.find('a', string=symbol)
    script_data = tag.find_parent('tr')

    # Creating a dictionary to store detail of the company.
    company = {}
    name = (script_data.select('a')[0]).get_text()
    start = (script_data.select('td:nth-child(4)')[0]).get_text()
    highest = (script_data.select('td:nth-child(5)')[0]).get_text()
    lowest = (script_data.select('td:nth-child(6)')[0]).get_text()
    end = (script_data.select('td:nth-child(7)')[0]).get_text()
    change = (script_data.select('td:nth-child(15)')[0]).get_text()
    company.update(
        {'company': name, 'open': start, 'previous close': end, 'high': highest, 'low': lowest, 'change': change})
    return company


