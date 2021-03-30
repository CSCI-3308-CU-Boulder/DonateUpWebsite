#class = "mainPrice"
#class = "nontranslate" id = prcIsum itemprop = "price" 
#content = (price)

# make a request to the ebay.com and get a page
# collect data from each detail page
# Collect all links to detail pages of each product
# write scraped data to csv file
import requests
from bs4 import BeautifulSoup
import re
from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("PayPallTest.html")

@app.route("/price", methods=['POST', 'GET'])
def price(scrapedValue):
    price = 20
    return render_template('PayPallTest.html', price = scrapedValue)

def get_page(url):
    response = requests.get(url)
    if not response.ok: #if failed
        print("failed server request \n")
        return
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

def get_detail_data(soup):
    #title id = itemTitle
    #price id = prcIsum
    #h1 = soup.find('span', id='prcIsum').get('content')
    h1 = soup.find('span', id='prcIsum').get('content')
    #h1 = soup.find('div').find('class', id = 'od-subtotals')
    #h1 = int(re.search('[0-9]+',h1).group(0))
    print(h1)
    return h1

def main():
    url = "https://www.ebay.com/itm/25-Amazon-Gift-Card-in-Gift-Box-Super-Fast-Shipping/324451167326?hash=item4b8acbec5e:g:P10AAOSw8Ntf19~f"
    #url = "https://www.amazon.com/gp/your-account/order-details?ie=UTF8&orderID=111-5653505-3572259&ref_=pe_386300_440135490_TE_simp_od&"
    get_detail_data(get_page(url))

if __name__ == '__main__': 
    main()
    app.run(debug = True)

# try:
#     pass
# else: