import csv
from pathlib import Path
import requests
from bs4 import BeautifulSoup

url = "https://novatec.com.br/categoria/banco-de-dados/?pag=1"

response = requests.get(url, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

livros = soup.find_all("div", class_="list-item")

dados_livros = []

print("Quantidade de livros encontrados:", len(livros))
print("-" * 40)


for livro in livros:
    titulo = livro.find("p", class_="list-title").a.get_text(strip=True)
    link = livro.find("p", class_="list-title").a["href"]
    url_livro = "https://novatec.com.br" + link
    
    response_livro = requests.get(url_livro, timeout=30)
    response_livro.raise_for_status()

    soup_livro = BeautifulSoup(response_livro.text, "html.parser")

    preco = soup_livro.find("span", class_="pp-price")


    if preco:
        valor = preco.get_text(strip=True)
    else:
        valor = "Preço não encontrado"

    dados_livros.append([titulo, valor, url_livro])
    
    print(f"Título: {titulo}")
    print(f"Preço: {valor}")
    print(f"Link: {link}")
    print("-" * 40) # Separador em traços
  
caminho_arquivo = Path("data/raw/livros.csv")

with caminho_arquivo.open(
    "w", newline="", encoding="utf-8-sig"
) as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")

    escritor.writerow(["titulo", "preco", "url"])
    escritor.writerows(dados_livros)

print(f"Total de livros salvos: {len(dados_livros)}")
print(f"Arquivo salvo em: {caminho_arquivo}")
