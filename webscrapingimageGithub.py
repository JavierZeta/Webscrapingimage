from turtle import screensize
import requests 
from bs4 import BeautifulSoup as bs 

github_name = input('Github name: ') 
url = 'https://github.com/'+github_name
r = requests.get(url)
soup  = bs(r.content, 'html.parser')
profile_image= soup.find('img', {'alt':'Avatar'})['src']
print(profile_image)