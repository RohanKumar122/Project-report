import requests
import html5lib
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# check status code for response received
# success code - 200
# print(r)
 
# print content of request
# print(r.status_code)
print(r.content)