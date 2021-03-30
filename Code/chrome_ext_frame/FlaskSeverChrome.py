#class = "mainPrice"
#class = "nontranslate" id = prcIsum itemprop = "price" 
#content = (price)

# make a request to the ebay.com and get a page
# collect data from each detail page
# Collect all links to detail pages of each product
# write scraped data to csv file
from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("popup.html")

@app.route("/", methods=['POST', 'GET'])
def price():
    FTest = "IT WORKS!"
    return render_template('popup.html', FlaskTest = FTest)

if __name__ == "__main__":
    app.run(debug=True)

# try:
#     pass
# else: