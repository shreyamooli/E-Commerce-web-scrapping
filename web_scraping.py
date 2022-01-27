# import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.amazon.in/HP-Processor-Windows-Natural-14s-dq2535TU/dp/B0928NL6F3/ref=sr_1_22?fst=as%3Aoff&pf_rd_i=16092374031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=6eb0a29c-ee06-43a5-b36a-a891cebbde27&pf_rd_r=CNHNZNJBNJGSRPAADA67&pf_rd_s=merchandised-search-7&pf_rd_t=101&qid=1642790288&refinements=p_85%3A10440599031%2Cp_n_feature_thirteen_browse-bin%3A12598162031%2Cp_72%3A1318477031&rnid=1318475031&rps=1&s=computers&sr=1-22'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36", "Accept-Encoding": "gzip, deflate","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text(strip=True)
#print(title)

prices = soup2.find('span', {'class': 'a-offscreen'}).get_text(strip=True)
#print(prices)

rating = soup2.find('span', {'class': 'a-icon-alt'}).get_text(strip=True)
#print(rating)


link = 'https://www.amazon.in/HP-Processor-Windows-Natural-14s-dq2535TU/product-reviews/B0928NL6F3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
page = requests.get(link)


soup = BeautifulSoup(page.content, 'html.parser')
 #print(soup.prettify())'

names = soup.find_all('span', {'class': 'a-profile-name'})
cust_name = []
for i in range(0, len(names)):
    cust_name.append(names[i].get_text())
#print(cust_name)


title1 = soup.find_all('a', class_='review-title-content')
review_title = []
for i in range(0, len(title1)):
    review_title.append(title1[i].get_text())
review_title[:] = [titles.lstrip('\n') for titles in review_title]
 #print(review_title)
review_title[:] = [titles.rstrip('\n') for titles in review_title]
#print(review_title)

data=[[title,prices,rating,cust_name,review_title]]
#print(data)

df=pd.DataFrame(data,columns=['title','prices','rating','cust_name','review_title'])
print(df)
df.to_csv('pagedata.csv')
