# Introdução ao Django 4 + CRUD completo com banco de dados

- Este projeto foi criado a partir do curso: https://www.udemy.com/share/106Y1S3@mlcWq6FBwum8rTU-Cqx--U64hCDx57qQdx87n_9c0k60xXmdXOYxEsBiQp9rWG7r/
- Obs: código comentado

## INSTRUÇÕES INICIAIS:

- 1ª Passo: Instalar o python
- 2º Passo: Instalar o visual studio code
- 3º Passo: Abrir o terminal Command Prompt no vs code

### ISOLAR DEPENDÊNCIAS
```js
python -m venv cliente
```

### ATIVAR VENV
```js
cd cliente
```
```js
cd Scripts
```
```js
activate
```

### RETORNAR PARA A PASTA DE ORIGEM
```js 
cd ..
```

### INSTALAR O DJANGO DENTRO DA VENV
```js
pip install django
```

### CRIAR UM PROJETO DJANGO
```js
django-admin startproject app .
```
- O arquivo manage.py é para rodar comandos do django
- O arquivo settings.py fica as configurações do sistema 

### RODAR O PROJETO DJANGO
```js
python manage.py runserver
```

### URLS
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/login/?next=/admin/

### CRIAR BANCO DE DADOS
```js
python manage.py migrate
```
### CRIAR SUPER USUÁRIO
```js
python manage.py createsuperuser 
```
- digitar user (ex: admin)
- digitar password (ex: 123456)

### ALTERAR BANCO DE DADOS E CRIAR TABELA
```js
python manage.py makemigrations
```
```js
python manage.py migrate
```

### CRIAR APLICATIVO
- Cada core é responsável por uma parte do sistema
```js
python manage.py startapp core
```
- Ao criar um core, não esquecer de registrar a aplicação no arquivo settings.py e urls.py na pasta app

### FLUXO DE LEITURA
- Uma request chega no servidor e verifica se a url existe, bate em uma view que acessa o banco de dados através de dos models, e retorna um template.
