'''
Version : 1.0
NLTK  Sentiment Analysis - www.amazon.in/
Scripted by : Sasmita Tripathy
Description: Extracting the review comment for Apple iPhone 11
'''

from requests_html import HTMLSession
from bs4 import BeautifulSoup


#accepting the order from user
order_item = input('''please enter the item you want to order from amazon:
"1" for "Apple iPhone 11" : ''')


#url for the product:
if order_item == "1":
    webURL = "https://www.amazon.in/Apple-iPhone-11-64GB-White/dp/B07XVMCLP7/ref=sr_1_1_sspa?dchild=1&keywords=Apple+iPhone+11&qid=1603268681&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVFI5UTNHWVo0UFhYJmVuY3J5cHRlZElkPUExMDEyNjM4MkJHMUk2N0xXWTlNRyZlbmNyeXB0ZWRBZElkPUEwNDgyMjM0Rkg0VDYyNzVITkVLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==#customerReviews"
else:
    exit()


#make a request to get the data from the site
session = HTMLSession()
resp = session.get(webURL)
print(resp)
soup = BeautifulSoup(resp.html.html, 'html.parser')
#print(soup)
jobElems = soup.find_all('div', class_='a-expander-content reviewText review-text-content a-expander-partial-collapse-content')
#print(jobElems)

#fetching the review details
count=0
for job_elem in jobElems:
    rev_detail = job_elem.span.text.strip()
    print(rev_detail)
    count=count+1
    print(count)
