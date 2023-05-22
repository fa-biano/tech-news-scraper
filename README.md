# 🔎 Projeto Tech News Scraper!

Esse projeto utiliza técnicas de raspagem de dados para buscar notícias de tecnologia no site https://blog.betrybe.com. </br>
As notícias raspadas do site são armazenadas no banco de dados MongoDB.

Toda interação ocorre no menu exibido no terminal, onde é possível escolher a qtd de notícias que deseja buscar e aplicar filtros de busca posteriomente.

Menu de opções:

`Selecione uma das opções a seguir:` </br>
` 0 - Popular o banco com notícias;` </br>
` 1 - Buscar notícias por título;` </br>
` 2 - Buscar notícias por data;` </br>
` 3 - Buscar notícias por categoria;` </br>
` 4 - Listar top 5 categorias;` </br>
` 5 - Sair.`

O desenvolvimento desse projeto foi realizado durante o curso de Desenvolvimento Web na [Trybe](https://www.betrybe.com/)!

## 🔥 Tecnologias utilizadas:

  * Python
  * Pytest
  * Parsel
  * Pymongo (MongoDB)

## ✨ Inicializando:

  Clone o repositório: `git clone git@github.com:fa-biano/tech-news-scraper.git`

  Execute no terminal `python3 -m venv .venv && source .venv/bin/activate` para habilitar o ambiente virtual

  Instale as dependências  com `python3 -m pip install -r dev-requirements.txt`. </br> 
  *(Algumas depedências do pytest precisam de pré-instalação de alguns pacotes, por isso, caso apresente algum erro no terminal, basta executar o comando de instalação novamente.)*

  Suba um container Docker com o MongoDB, executando o comando `docker compose up -d`.
  
  No terminal, execute o modulo com as funções do scraper para mostrar o menu de opções, através do comando `tech-news-analyzer` no diretorio raiz.
