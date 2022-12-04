import requests
from bs4 import BeautifulSoup

 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# soup =BeautifulSoup(r.content,"html5lib")
soup =BeautifulSoup(r.text,'html.parser')

print(soup)
# print(soup.prettify)
# print(soup.title)
# title =soup.title
# print(title)
# print(type(title.string))