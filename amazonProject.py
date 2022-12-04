from bs4 import BeautifulSoup as bs
import requests

URL ="https://www.amazon.in/s?i=electronics&bbn=1805560031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_6%3AA14CZOWI0VEHLG%7CA1P3OPO356Q9ZB%7CA2HIN95H5BP4BL%2Cp_89%3AApple&ref=mega_elec_s23_1_2_1_6"

# URL ="https://www.amazon.in/s?k=iphone&rh=n%3A1389401031&ref=nb_sb_noss"
# URL ="https://www.amazon.in/s?i=electronics&bbn=1805560031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_6%3AA14CZOWI0VEHLG%7CA1P3OPO356Q9ZB%7CA2HIN95H5BP4BL%2Cp_89%3AApple&ref=mega_elec_s23_1_2_1_6"


r =requests.get(URL)

# print(r)


soup =bs(r.content,'html.parser')

# print(soup)
# print(soup.prettify())
# print(r.content)

names =soup.find_all('span',class_='a-price-whole')
# print(names)
# print(names.content)
# for i in names:
#     print(i.content)

lst =[]

for i in range(0,len(names)):
    lst.append(names[i].get_text())

print(lst)

# for i in range(0,len(lst)):
#     print(i)    

for i in lst:
    print(i)



