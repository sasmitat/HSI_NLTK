'''
Version : 1.0
NLTK  Sentiment Analysis - www.amazon.in/
Scripted by : Sasmita Tripathy
Description: Extracting the review comment for Apple iPhone 11
'''

from requests_html import HTMLSession
from bs4 import BeautifulSoup

# accepting the order from user
order_item = input('''please enter the item you want to order from amazon:
"1" for "Apple iPhone 11" : ''')

# url for the product:
if order_item == "1":
    webURL = "https://www.amazon.in/Apple-iPhone-11-64GB-White/dp/B07XVMCLP7/"
else:
    exit()

# make a request to get the data from the site
session = HTMLSession()
resp = session.get(webURL)
print(resp)
soup = BeautifulSoup(resp.html.html, 'html.parser')
# print(soup)

reviews = soup.find_all('div',
                    class_='a-expander-content reviewText review-text-content a-expander-partial-collapse-content')

# fetching the review details
count = 0
for review in reviews:
    rev_detail = review.span.text.strip()
    print(rev_detail)
    count = count + 1
    print(count)


review_dates = soup.findAll('span',
    {'data-hook':'review-date',
     'class': 'a-size-base a-color-secondary review-date'})

# fetching the review place and dates
count = 0
for review_date in review_dates:
    rev_date_detail = review_date.text.strip()
    print(rev_date_detail)
    count = count + 1
    print(count)
