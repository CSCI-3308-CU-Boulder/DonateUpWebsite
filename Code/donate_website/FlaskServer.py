#class = "mainPrice"
#class = "nontranslate" id = prcIsum itemprop = "price" 
#content = (price)

# make a request to the ebay.com and get a page
# collect data from each detail page
# Collect all links to detail pages of each product
# write scraped data to csv file
from flask import Flask, render_template, redirect, url_for, request
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ur = "from EbayPriceScrape import scrapedValue"

@app.route("/")
def index():
    return render_template("DonateUp_home.html")

@app.route("/price", methods=['POST', 'GET'])
def price():
    price = 0
    if request.method == 'POST':
        url = request.form['nm']
        print(url)
        from EbayPriceScrape import main
        price = main(url)
        return render_template('DonateUp_home.html', price = price)
    else:
      user = request.args.get('nm')
      return render_template('DonateUp_home.html', price = price)

if __name__ == "__main__":
    app.run(debug=True)

# try:
#     pass
# else: