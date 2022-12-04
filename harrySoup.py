import requests
from bs4 import BeautifulSoup

 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
# r = requests.get('https://webscraper.io/test-sites')

soup =BeautifulSoup(r.content,'html.parser')

title =soup.title
# print(title)
# print(type(title.string))


# // Get all paras from the page

# paras =soup.find_all('p')
# print(paras)
'''
# // Get all anchors from the page

anchors =soup.find_all('a')
# print(anchors)

for line in anchors:
    print(line.get('href')) '''
images_list = []
 
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
     
for image in images_list:
    print(image)