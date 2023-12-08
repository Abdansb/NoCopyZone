import requests
from bs4 import BeautifulSoup


website = "https://livescore90bola.com/"

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")

print(soup.prettify())
