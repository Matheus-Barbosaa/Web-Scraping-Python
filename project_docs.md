# Comandos Python utilizados no projeto

## 1. Importar bibliotecas

    import requests
    from bs4 import BeautifulSoup
    import csv
    from pathlib import Path

**Função das bibliotecas:**

- `requests`: realiza requisições HTTP.
- `BeautifulSoup`: interpreta o HTML e permite localizar elementos.
- `csv`: grava os dados em um arquivo CSV.
- `Path`: facilita a manipulação de caminhos de arquivos e pastas.

## 2. Definir a URL e acessar a página

    url = "https://novatec.com.br/categoria/banco-de-dados/?pag=1"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

**Comandos utilizados:**

- `requests.get()`: acessa a página.
- `timeout=30`: define um limite de espera de 30 segundos.
- `raise_for_status()`: gera um erro caso a resposta HTTP indique falha.

## 3. Interpretar o HTML

    soup = BeautifulSoup(response.text, "html.parser")

Converte o conteúdo HTML da resposta em uma estrutura que pode ser pesquisada.

## 4. Localizar os livros

    livros = soup.find_all("div", class_="list-item")

Localiza os elementos HTML que representam os livros na página da categoria.

## 5. Extrair título e link

    titulo = livro.find("p", class_="list-title").a.get_text(strip=True)
    link = livro.find("p", class_="list-title").a["href"]
    url_livro = "https://novatec.com.br" + link

**Comandos utilizados:**

- `find()`: localiza um elemento HTML.
- `get_text(strip=True)`: extrai o texto e remove espaços desnecessários nas extremidades.
- `["href"]`: acessa o atributo que contém o link.

## 6. Acessar a página individual do livro

    response_livro = requests.get(url_livro, timeout=30)
    response_livro.raise_for_status()

    soup_livro = BeautifulSoup(response_livro.text, "html.parser")

Realiza uma nova requisição para obter informações disponíveis na página individual do produto.

## 7. Extrair o preço

    preco = soup_livro.find("span", class_="pp-price")

    if preco:
        valor = preco.get_text(strip=True)
    else:
        valor = "Preço não encontrado"

Localiza o elemento que contém o preço. Se não for encontrado, registra uma mensagem informativa.

## 8. Armazenar os dados em uma lista

    dados_livros.append([titulo, valor, url_livro])

Adiciona título, preço e URL à lista que será exportada para CSV.

## 9. Criar o caminho do arquivo CSV

    caminho_arquivo = Path("data/raw/livros.csv")

Define o caminho do arquivo de saída a partir da pasta principal do projeto.

## 10. Exportar os dados para CSV

    with caminho_arquivo.open(
        "w", newline="", encoding="utf-8-sig"
    ) as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(["titulo", "preco", "url"])
        escritor.writerows(dados_livros)

**Parâmetros e métodos utilizados:**

- `"w"`: abre o arquivo para escrita, substituindo o conteúdo anterior.
- `encoding="utf-8-sig"`: ajuda na compatibilidade de caracteres acentuados com ferramentas como o Excel.
- `delimiter=";"`: utiliza ponto e vírgula para separar as colunas.
- `writerow()`: grava o cabeçalho.
- `writerows()`: grava os registros coletados.

## 11. Executar o projeto pelo terminal

    python src/coletar_livros.py

