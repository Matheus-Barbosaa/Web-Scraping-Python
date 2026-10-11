
import requests
from bs4 import BeautifulSoup

url = "https://novatec.com.br/livros/web-scraping-com-python-3ed/"

response = requests.get(url, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

capa = soup.find("img", alt="Web Scraping com Python - 3ª Edição")
preco = soup.find("span", class_="pp-price")

print(capa["alt"])
print(preco.get_text(strip=True))
