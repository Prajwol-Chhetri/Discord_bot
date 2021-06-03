# IMPORTING THE REQUIRED MODULES TO SCRAPE REQUIRED DATA
import requests
from bs4 import BeautifulSoup


def gainers():
    # this function returns the details of top 10 gainers currently.
    res = requests.get('http://www.nepalstock.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    top_gainers = []

    # collecting data from the website
    company = soup.select('#top-gainers .row1 > td:nth-child(1)')[:10]
    ltp = soup.select('#top-gainers .row1 > td:nth-child(2)')[:10]
    point_change = soup.select('#top-gainers .row1 > td:nth-child(3)')[:10]
    percent_change = soup.select('#top-gainers .row1 > td:nth-child(4)')[:10]

    # Creating a dictionary to store detail of each company and adding them to a list to store top 10 gainers.
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


def losers():
    # this function returns the details of top 10 losers currently.
    res = requests.get('http://www.nepalstock.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    top_losers = []

    # collecting data from the website
    company = soup.select('#top-losers .row1 > td:nth-child(1)')[:10]
    ltp = soup.select('#top-losers .row1 > td:nth-child(2)')[:10]
    point_change = soup.select('#top-losers .row1 > td:nth-child(3)')[:10]
    percent_change = soup.select('#top-losers .row1 > td:nth-child(4)')[:10]

    # Creating a dictionary to store detail of each company and adding them to a list to store top 10 losers.
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
    # this function returns the current status of NEPSE.
    res = requests.get('http://www.nepalstock.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    nepse = {}

    # collecting data from the website
    status = ((soup.find("div", {"class": "market-status"}).find('b')).get_text()).strip()
    index = ((soup.find("div", {"class": "current-index"})).get_text()).strip()
    point_change = float(((soup.find("div", {"class": "point-change"})).get_text()).strip())
    percent_change = ((soup.find("div", {"class": "percent-change"})).get_text()).strip()

    # Creating a dictionary to store current status of NEPSE.
    nepse.update({'status': status, 'index': index, 'point-change': point_change, 'percent-change': percent_change})
    return nepse


def get_live_script(symbol):
    # this function returns the details of a certain company.
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

    # Creating a dictionary to store detail of the company and adding it to a list.
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

    # returning None in-case user enters wrong symbol for company.
    company = next((item for item in stocks if item['company'] == symbol), None)
    return company


