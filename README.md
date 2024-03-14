# Sistema de Gerenciamento de Dispositivos de Rede com Django

Este é um projeto de sistema de gerenciamento de dispositivos de rede desenvolvido usando Django, um framework web em Python.

## Descrição

Este projeto consiste em uma aplicação web que permite escanear a rede local em busca de dispositivos conectados e gerenciar esses dispositivos. Ele oferece as seguintes funcionalidades:

- Escaneamento da rede local para detectar dispositivos conectados.
- Listagem dos dispositivos encontrados, exibindo seus endereços IP, endereços MAC e nomes (se disponíveis).
- Adição de novos dispositivos conhecidos, fornecendo um nome para identificação.
- Adição de dispositivos desconhecidos para posterior identificação.

## Tecnologias Utilizadas

- Python
- Django
- Bootstrap (para a interface do usuário)

## Instalação e Uso

1. Clone este repositório em sua máquina local:

```
git clone https://github.com/seu_usuario/nome-do-repositorio.git
```

2. Navegue até o diretório do projeto:

```
cd nome-do-repositorio
```

3. Crie um ambiente virtual para o projeto (recomendado):

```
python -m venv venv
```

4. Ative o ambiente virtual:

- No Windows:

```
venv\Scripts\activate
```

- No macOS e Linux:

```
source venv/bin/activate
```

5. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

6. Execute as migrações do Django para criar o banco de dados:

```
python manage.py migrate
```

7. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

8. Acesse o aplicativo em seu navegador:

```
http://localhost:8000/
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues para relatar problemas ou sugestões de melhorias.
