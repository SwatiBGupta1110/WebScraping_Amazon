import requests


# proxy works as  a intermediate server --> request first goes to proxy provider and then to destination
# We can use 3 party proxy providers to use a rotating proxy to scrape a website
proxies = {
"http":"http://10.10.1.10:3128",
"https": "http://10.10.1.10:1080",

}

# r = requests.get("https://api64.ipify.org?format=json", proxies=proxies) # Ip cgange karte hue scraping ko barkarar rakhna
# print(r.json())

# IP address api to fetch ip adrress of my laptop
# https://whatismyipaddress.com/ip/82.27.86.132  --> ip address lookup

r = requests.get("https://api64.ipify.org?format=json") # Ip change karte hue scraping ko barkarar rakhna
print(r.json())

