import requests
from bs4 import BeautifulSoup

res4 = requests.get('https://www.sharesansar.com/today-share-price')  # getting response from the website
print(res4)
soup4 = BeautifulSoup(res4.text, 'html.parser')  # changes the string from res.text to soup object using html parser
print(soup4)
stock_table = soup4.tbody  # getting the table containing stock details

# getting the contents from the table
company = stock_table.select('a')
start = stock_table.select('td:nth-child(4)')
highest = stock_table.select('td:nth-child(5)')
lowest = stock_table.select('td:nth-child(6)')
end = stock_table.select('td:nth-child(7)')
change = stock_table.select('td:nth-child(15)')


#  creating a function to append the stock details to a list
def create_custom_ss():
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

    return stocks


def get_script_detail(symbol):
    stocks = create_custom_ss()
    script = next((item for item in stocks if item['company'] == symbol), None)
    return script



