# Walmart Logistics

## Requisitos

1. Python 2.7
2. PostgreSQL 9.2
3. virtualenv
4. Linux ou Mac

## Instalação

Vá até o diretório de sua preferência para criar um ambiente virtual utilizando o virtualenv

- virtualenv logistics
- cd logistics
- source bin/activate

Em seguida clone o projeto

- git clone git@github.com:kureck/logistics.git

Entre no diretório do projeto criado e instale as dependências

- pip install -r requirements.txt

Uma vez instalados os requisitos rode o comando e siga os passos indicados

- python manage.py syncdb

Em seguida inicie o server

- python manage.py runserver

Daí será possível acessar o sistema no link http://127.0.0.1:8000/

## Como usar via interface web

Ao acessar o link será possível "Criar um Mapa" e listar os mapas existentes.

Os mapas possuem nome único e podem ser criados de duas formas:

* usando o campo de texto no formato A B 10 ou A,B,10 com quebra de linha para cada tupla
* a partir do upload de um arquivo CSV sem o header

Uma vez que tenha sido criado o mapa, pode-se encontrar os caminhos mais curtos ao passar a origem, destino, autonomia e valor do litro.


## Como usar via webservice

Para usar o webservice basta fazer um request via POST passando os parâmetros:

* road_map_name: nome do mapa
* origin: local de origem
* destination: local de destino
* autonomia: autonomia do veículo
* litro: valor do litro

Exemplo:

Crie um mapa com um nome qualquer e as direções e distâncias abaixo

| origem | destino | distância |
| ------ | ------- | --------- |
| A | B | 10 |
| B | D | 15 |
| A | C | 20 |
| C | D | 30 |
| B | E | 50 |
| D | E | 30 |

No terminal use o seguinte comando:

curl -i -H "Content-Type: application/json" -X POST -d '{"road_map_name":<nome-do-mapa>, "origin": "A", "destination":"D", "autonomia": 10, "litro":2.5 }' http://127.0.0.1:8000/shortest_path/api/map/find_shortest_path/

Nesse caso a resposta será em JSON: {"shortest_path": ["A", "B", "D"], "shortest_path_value": 6.25}