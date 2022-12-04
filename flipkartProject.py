import requests
from bs4 import BeautifulSoup as bs

url =('https://www.flipkart.com/mobile-phones-store?fm=neo%2Fmerchandising&iid=M_88797c02-3063-4d20-b457-5b8dfc5b1b75_1_372UD5BXDFYS_MC.ZRQ4DKH28K8J&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Mobiles_ZRQ4DKH28K8J&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=ZRQ4DKH28K8J')

r =requests.get(url)
print(r)

# print(r.content)
soup =bs(r.content,'html.parser')

title =soup.find_all('div',class_='_1W9f5C')
price =soup.find_all('div',class_='_30jeq3 UMT9wN')
# title =soup.find_all('div',class_='_2OosNL')

for i in range(0,len(title)):
    print(f'{title[i].get_text()} : {price[i].get_text()}')



# print(title.content)
# print(soup)