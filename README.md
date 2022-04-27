# ImagensDjangoRest
Upload de Imagens numa API Rest

## Tecnologias utilizadas
[Python 3.x]\
[Django]\
[Django rest framework]\
[SQLite]

## Instalação
Certifique-se de ter o Python 3 instalado, verifique a versão com o comando
```bash
python3 --version
```

Se não tiver, acesse o site (https://www.python.org/downloads/) para baixar e fazer a instalação

Faça uma cópia do projeto
```bash
git clone https://github.com/VictorHermon/ImagensDjangoRest.git
```

Instale o pacote abaixo, para criação do ambiente virtual, substitua o X pela sua versão do python
```bash
sudo apt install python3.x-venv
```

Dentro do diretorio do projeto, crie um ambiente virtual para instalar as dependências
```bash
python -m venv ./venv
```

Ative esse ambiente com o comando
```bash
source venv/bin/activate
```

Recomendo atualizar o gerenciador de pacotes pip
```bash
pip install --upgrade pip
```

Instale os modulos necessários para executar o projeto
```bash
pip install -r requirements.txt
```

Crie um arquivo (.env) e dentro dele defina a variavel DJANGO_SECRET_KEY com o valor gerado do codigo abaixo
```bash
python generate_secret_key.py
```

Gere os arquivos para fazer as migrações no banco
```bash
python manage.py makemigrations
```

E finalmente faça a migração
```bash
python manage.py migrate
```

## Execute a aplicação
Execute o codigo abaixo e abra o navegador no endereço:
http://localhost:8000
```bash
# development
python manage.py runserver
```
