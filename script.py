from bs4 import BeautifulSoup
import requests

website = 'https://tipsterarea.com/facts'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())