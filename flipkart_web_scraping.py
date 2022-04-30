import urllib.request
from bs4 import BeautifulSoup
import requests
import requests

url = requests.get("http://google.com")
htmltext = url.text
import pandas as pd

url = "https://www.flipkart.com/search?q=mi+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mi+mobiles%7CMobiles&requestId=89e1555f-faab-40da-b301-131cc5fefc34&as-backfill=on"

my_request = urllib.request.urlopen("INSERT URL HERE")

my_HTML = my_request.read().decode("utf8")

print(my_HTML)
req = requests.get(url)

#htmlcontent = response.content

#soup = BeautifulSoup(htmlcontent,"html.parser")

#print(soup.prettify)
content = BeautifulSoup(req.content, 'html.parser')

name = content.find_all('div', {"class": "_4rR01T"})
price = content.find_all('div', {"class": "_30jeq3 _1_WHN1"})
rating = content.find_all('div', {"class": "_3LWZlK"})

nm = []

pr = []

rt = []
for i in name:
    nm.append(i.text)

for i in price:
    pr.append(i.text)

for i in rating:
    rt.append(i.text)

data = {'NAME': nm, 'PRICE': pr, 'RATING': rt}
#print(data)


df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()

#df=pd.DataFrame(data)
print(df)
df.to_csv('file19.csv')
