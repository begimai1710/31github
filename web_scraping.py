import requests
from bs4 import BeautifulSoup

url = "https://bbc.com/news"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")
# for link in links:
    # print(link.get("href"))
print(soup)