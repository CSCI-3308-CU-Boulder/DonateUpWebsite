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
    #h1 = soup.find('span', id = 'pricebook_ourprice')
    h1 = int(re.search('[0-9]+',h1).group(0))
    print(h1 + 10)
    return h1

def main():
    url = "https://www.ebay.com/itm/25-Amazon-Gift-Card-in-Gift-Box-Super-Fast-Shipping/324451167326?hash=item4b8acbec5e:g:P10AAOSw8Ntf19~f"
    #url = "https://www.amazon.com/Mastercard-Gift-Card-plus-Purchase/dp/B07GFQ5B44/ref=sr_1_7?dchild=1&keywords=gift+card&qid=1615238714&sr=8-7"
    get_detail_data(get_page(url))

if __name__ == '__main__':
    main()

# try:
#     pass
# else: