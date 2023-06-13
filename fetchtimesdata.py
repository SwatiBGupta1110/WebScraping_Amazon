import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)     # url ka content nikal lo
    # print(r.text) # iski jagah ek save krte hai file me
    with open (path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/nagpur"


fetchAndSaveToFile(url, "timesofindia.html")