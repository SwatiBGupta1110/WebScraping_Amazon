import requests
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
    "http":"http://customer-rcodewithharry:ActicitXccR8xbss@pr.oxylabs.io.7777",
    "https":"http://customer-rcodewithharry:ActicitXccR8xbss@pr.oxylabs.io.7777"
}

data = {"title":[], "price":[]}
url = "https://www.amazon.in/s?k=iphone&crid=1B2BTLNKUUVUI&sprefix=iphone%2Caps%2C82&ref=nb_sb_noss_1"

#https://stackoverflow.com/questions/27652543/how-to-use-python-requests-to-fake-a-browser-visit-a-k-a-and-generate-user-agent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers= headers)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify)

spans = soup.find(class_="a-size-medium")
print(spans)

div = soup.select("div.sg-col-inner")  # div.sg-col-inner --> is a element.class
print(div)

# to get the title
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
# print(spans)

prices = soup.select("span.a-price")
# print(prices)

for span in spans:
    print(span.string)
    data["title"].append(span.string)

# To scrape price
#With the help of js write document.querySelectorAll("span.a-price") in Console
for price in prices:
    if not("a-text-price" in price.get("class")): # Show prices only when a-text-price thsi class is not there as it shows teh original price and not the discounted price
        print(price.find("span").get_text())  # get_text() function se hum andar ka text prapt kar skte hai
        data["price"].append(price.find("span").get_text())

        # apply a check as program is taking other recommended price also, break a program when 
        # data title gets equal to data price length
        if(len(data["price"] == len(data["title"]))):
            break # break out of the loop

df= pd.DataFrame.from_dict(data)

df.to_excel("data.xlsx",index = False)
