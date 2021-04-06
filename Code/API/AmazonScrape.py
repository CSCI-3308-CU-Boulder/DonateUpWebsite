
import requests
from bs4 import BeautifulSoup
import re
from flask import Flask, render_template
import validators

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_page(url):
    response = requests.get(url, headers=headers)
    if not response.ok: #if failed
        print("failed server request \n")
        return 'failed'
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        #print(soup)
        return soup

def get_detail_data(soup):
    h1 = soup.find('span', {"id":"priceblock_saleprice"}).text
    #h1 = soup.find('input', {"id":"attach-base-product-price"}).get('value')
    #<span id="priceblock_saleprice" class="a-size-medium a-color-price priceBlockSalePriceString">$129.99</span>
    #<input type="hidden" id="attach-base-product-price" value="129.99">
    
    print(h1)
    return h1

def main(url):
    if(validators.url(url)):
        scrapedValue = get_detail_data(get_page(url))
        return scrapedValue
    else:
        print("invlaid URL")
        return "invalid URL"


if __name__ == '__main__': 
    url = "https://www.amazon.com/FEICE-Stainless-Leathers-Waterproof-Business/dp/B074MWWTVL"
    main(url)