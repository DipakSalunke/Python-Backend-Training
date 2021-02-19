import requests
from bs4 import BeautifulSoup 
r = requests.get('https://pypi.org/project/requests/')
soup = BeautifulSoup(r.text,'html.parser') 
print("Title of the website is : ") 
print(soup.title.get_text())