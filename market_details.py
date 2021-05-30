import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.sharesansar.com/today-share-price')  # getting response from the website
soup = BeautifulSoup(res.text, 'html.parser')  # changes the string from res.text to soup object using html parser
stock_table = soup.tbody  # getting the table containing stock details

# getting the contents from the table
company = stock_table.select('a')
start = stock_table.select('td:nth-child(4)')
highest = stock_table.select('td:nth-child(5)')
lowest = stock_table.select('td:nth-child(6)')
end = stock_table.select('td:nth-child(7)')
change = stock_table.select('td:nth-child(15)')

# creating lists to store top 5 gainers and losers
top_gainers = []
top_losers = []

# creating a function that sorts the stocks according to their change
def sort_stocks_by_change(stock_list):
    return sorted(stock_list, key=lambda k: k['change'], reverse=True)


#  creating a function to append the stock details to a list
def create_custom_ml(company, start, highest, lowest, end, change):
    stocks = []
    for idx, item in enumerate(company):
        name = company[idx].getText()
        close_price = end[idx].getText()
        diff_price = float(change[idx].getText())
        high_price = highest[idx].getText()
        low_price = lowest[idx].getText()
        opening_price = start[idx].getText()
        stocks.append({'company': name, 'open': opening_price, 'previous close': close_price, 'high': high_price,
                       'low': low_price,
                       'change': diff_price})
    return sort_stocks_by_change(stocks)


stocks_list = create_custom_ml(company, start, highest, lowest, end, change)


def summary():
    top_gainers.append(stocks_list[:4])
    top_losers.append(list(reversed(stocks_list[-5:])))
    return top_gainers, top_losers
