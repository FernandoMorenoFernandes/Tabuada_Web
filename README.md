# Gerador de Tabuada Web

Esta é uma simples aplicação web para gerar tabuadas. Ela foi construída usando Python 3.11.4, o framework Flask 2.2.3. A aplicação permite que os usuários escolham um número e vejam a tabuada correspondente.

## Pré-requisitos

Certifique-se de ter Python 3.11.4 instalado em seu sistema. Você pode verificar a versão do Python com o seguinte comando:

```bash
python --version
```
Caso não tenha o python instalado você poderá instalar conforme o seu sistema operacional acessando o site oficial do Python: https://www.python.org/

Você também precisará instalar o Flask. Você pode instalá-los usando o pip:

```bash
pip install Flask
```

## Como Executar
### 1. Clone este repositório em sua máquina local:

git clone https://github.com/FernandoMorenoFernandes/Tabuada_Web.git

### 2. Navegue até o diretório do projeto:

```bash
cd gerador-de-tabuada-web
```
### 3. Execute a aplicação:

```bash
python app.py
```
## Uso
1. Abra a aplicação em seu navegador.
2. Escolha um número para o qual você deseja gerar a tabuada.
3. Clique no botão "Gerar Tabuada".
4. A tabuada correspondente será exibida na página.

# Como Executar com Docker
## Pré-requisitos

Docker instalado em seu sistema.

Certifique-se de ter o Docker instalado em sua máquina. Você pode verificar a instalação do Docker com o seguinte comando:

```bash
docker --version
```
Caso não tenha o docker instalado acesse o link do site oficial do Docker para correta instalação no seu sistema operacional:
https://docs.docker.com/engine/install

## Configuração do Docker

### 1. Com o repositório clonado em sua máquina local, navegue até o diretório do projeto:

```bash
cd gerador-de-tabuada-web
```
### 2. Construa a imagem Docker:

```bash
docker build -t gerador-de-tabuada-web .
```
### 3. Execute o container Docker:

```bash
docker run -p 5000:5000 gerador-de-tabuada-web
```
A aplicação estará rodando em http://localhost:5000 no seu navegador.

## Uso
1. Abra a aplicação em seu navegador.
2. Escolha um número para o qual você deseja gerar a tabuada.
3. Clique no botão "Gerar Tabuada".
4. A tabuada correspondente será exibida na página.
