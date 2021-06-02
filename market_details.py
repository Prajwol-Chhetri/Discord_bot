import requests
from bs4 import BeautifulSoup


def gainers(soup):
    top_gainers = []
    company = soup.select('#top-gainers .row1 > td:nth-child(1)')[:10]
    ltp = soup.select('#top-gainers .row1 > td:nth-child(2)')[:10]
    point_change = soup.select('#top-gainers .row1 > td:nth-child(3)')[:10]
    percent_change = soup.select('#top-gainers .row1 > td:nth-child(4)')[:10]

    for idx, item in enumerate(company):
        name = company[idx].getText()
        last_traded_price = ltp[idx].getText()
        diff_price = point_change[idx].getText()
        change = percent_change[idx].getText()
        top_gainers.append({
            'company': name,
            'LTP': last_traded_price,
            'diff_price': diff_price,
            'change': change
        })

    return top_gainers


def losers(soup):
    top_losers = []
    company = soup.select('#top-losers .row1 > td:nth-child(1)')[:10]
    ltp = soup.select('#top-losers .row1 > td:nth-child(2)')[:10]
    point_change = soup.select('#top-losers .row1 > td:nth-child(3)')[:10]
    percent_change = soup.select('#top-losers .row1 > td:nth-child(4)')[:10]

    for idx, item in enumerate(company):
        name = company[idx].getText()
        last_traded_price = ltp[idx].getText()
        diff_price = point_change[idx].getText()
        change = percent_change[idx].getText()
        top_losers.append({
            'company': name,
            'LTP': last_traded_price,
            'diff_price': diff_price,
            'change': change
        })

    return top_losers


def market_status():
    res = requests.get('http://www.nepalstock.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    nepse = []

    status = ((soup.find("div", {"class": "market-status"}).find('b')).get_text()).strip()
    index = ((soup.find("div", {"class": "current-index"})).get_text()).strip()
    point_change = float(((soup.find("div", {"class": "point-change"})).get_text()).strip())
    percent_change = ((soup.find("div", {"class": "percent-change"})).get_text()).strip()

    top_losers = losers(soup)
    top_gainers = gainers(soup)

    nepse.extend([{'status': status, 'index': index, 'point-change': point_change, 'percent-change': percent_change}, top_losers, top_gainers])
    return nepse


def get_live_script(symbol):
    res2 = requests.get('http://www.nepalstock.com/stocklive')
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    stock_table = soup2.find('tbody')
    stocks = []

    # storing details of the company in respective variables
    company = stock_table.select('td:nth-child(2)')
    ltp = stock_table.select('td:nth-child(3)')
    diff_price = stock_table.select('td:nth-child(6)')
    start = stock_table.select('td:nth-child(7)')
    highest = stock_table.select('td:nth-child(8)')
    lowest = stock_table.select('td:nth-child(9)')
    close_price = stock_table.select('td:nth-child(11)')

    for idx, item in enumerate(company):
        name = company[idx].getText()
        last_traded_price = ltp[idx].getText()
        change = float(diff_price[idx].getText())
        opening_price = start[idx].getText()
        high_price = highest[idx].getText()
        low_price = lowest[idx].getText()
        closing = close_price[idx].getText()
        stocks.append({
            'company': name,
            'LTP': last_traded_price,
            'open': opening_price,
            'previous-close': closing,
            'high': high_price,
            'low': low_price,
            'change': change
        })

    company = next((item for item in stocks if item['company'] == symbol), None)
    return company

