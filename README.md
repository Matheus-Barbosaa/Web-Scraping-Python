# Web Scraping com Python

## Sobre o projeto

Este projeto tem como objetivo praticar Web Scraping com Python para coletar informações de livros disponíveis no catálogo da Editora Novatec.

A proposta é acessar uma página de livros, extrair informações das páginas individuais dos produtos, organizar os dados coletados e exportar os resultados para um arquivo CSV, facilitando análises posteriores.

## Objetivos

- Praticar a coleta de dados de páginas web.
- Fazer requisições HTTP com `Requests`.
- Extrair informações HTML com `BeautifulSoup`.
- Coletar títulos, preços e links dos livros.
- Organizar os dados em uma lista.
- Exportar os resultados para CSV.
- Praticar a organização e o versionamento de um projeto Python.

## Tecnologias utilizadas

- Python
- Requests
- BeautifulSoup
- CSV
- Git e GitHub

## Dados coletados

O projeto utiliza o catálogo de livros da [Editora Novatec](https://novatec.com.br/), com a categoria de Banco de Dados como ponto de partida.

Os dados coletados incluem:

- Título do livro
- Preço
- Link da página do livro

## Resultados

Durante a execução do projeto, foram coletados 10 livros. As informações foram organizadas e salvas no arquivo `data/raw/livros.csv`, utilizando ponto e vírgula como separador das colunas.

## Como executar

1. Clone este repositório.
2. Crie e ative um ambiente virtual Python.
3. Instale as dependências listadas em `requirements.txt`.
4. Execute o script de coleta.
5. Confira o arquivo CSV gerado.

Para consultar as explicações dos comandos Python utilizados no desenvolvimento, acesse o arquivo `PROJECT_DOCS.md`.

## Aprendizados

Este projeto faz parte do meu desenvolvimento em Análise de Dados, com foco na coleta, organização e preparação de dados utilizando Python.

Durante o desenvolvimento, pratiquei requisições HTTP, extração de informações do HTML, acesso às páginas individuais dos produtos e exportação dos dados para CSV.

## Autor

**Matheus Barbosa**


