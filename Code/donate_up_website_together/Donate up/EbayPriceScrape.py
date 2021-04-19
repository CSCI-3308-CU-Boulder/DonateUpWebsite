
import requests
from bs4 import BeautifulSoup
import re
from flask import Flask, render_template
import validators


def get_page(url):
    response = requests.get(url)
    if not response.ok: #if failed
        print("failed server request \n")
        return 'failed'
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

def get_detail_data(soup):

    h1 = soup.find('span', id='prcIsum').get('content')
    #h1 = soup.find('span', id='prcIsum')
    print(h1)
    return h1

def main(url):
    if(validators.url(url)):
        scrapedValue = get_detail_data(get_page(url))
        return float(scrapedValue)
    else:
        print("invlaid URL")
        return "invalid URL"


if __name__ == '__main__': 
    #url = "https://www.ebay.com/itm/25-Amazon-Gift-Card-in-Gift-Box-Super-Fast-Shipping/324451167326?hash=item4b8acbec5e:g:P10AAOSw8Ntf19~f"
    main(url)