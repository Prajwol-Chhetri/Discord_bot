import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.nepalstock.com/')  # summary of nepse
# changes the string from res.text to soup object using html parser
soup = BeautifulSoup(res.text, 'html.parser')


def market_status():
    status = soup.find("div", {"class": "market-status"}).find('b')
    if status.get_text() == "Market Open":
        return True
    else:
        return False


def get_script_detail(symbol):
    res2 = requests.get('http://www.nepalstock.com/stocklive')  # live market
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    live_table = soup2.find('tbody')
    stocks = []

    # storing details of the company in respective variables
    company = live_table.select('td:nth-child(2)')
    ltp = live_table.select('td:nth-child(3)')
    diff_price = live_table.select('td:nth-child(6)')
    start = live_table.select('td:nth-child(7)')
    highest = live_table.select('td:nth-child(8)')
    lowest = live_table.select('td:nth-child(9)')

    for idx, item in enumerate(company):
        name = company[idx].getText()
        last_traded_price = ltp[idx].getText()
        change = float(diff_price[idx].getText())
        opening_price = start[idx].getText()
    high_price = highest[idx].getText()
    low_price = lowest[idx].getText()
    stocks.append({
        'company': name,
        'LTP': last_traded_price,
        'open': opening_price,
        'high': high_price,
        'low': low_price,
        'change': diff_price
    })

    company = next((item for item in stocks if item['company'] == symbol), None)
    return company


