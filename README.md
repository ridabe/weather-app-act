
![Logo](https://carreiras.raizen.com.br/wp-content/webp-express/webp-images/uploads/2022/03/logo_raizen.png.webp)


# Raízen Teste

O desafio é elaborar uma aplicação de backend utilizando a linguagem de programação Python que deverá conter 
uma API retornando os dados da previsão do tempo dos próximos dias. Para elaborar essa aplicação, 
utilizar a API de previsão do tempo de 5 dias do https://openweathermap.org/.

A minha proposta como desenvolvedor foi trazer o ambinete o mais proximo possivel da vida real, utilizando 
a base Mongo diretamente do servidor mongoDB, simulando as configurações que um Devops deveria fazer, como a inserção do
IP da maquina que esta hospedando os serviços.


## Etiquetas

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Resumo do sistema

Através desta Api, o sistema envia uma requisição para a url proposta no teste, recupera os dados da precisão do tempo para a cidade selecionada e salva o historico desta busca na base de dados. 


## Stack utilizada

**Back-end:** 
- Python

**Framework:** 
- FastApi

**Bibliotecas:**
- requests;
- pymongo;
- datetime;
- dotenv.

## Configurando o ip da mauina no MongoAtlas
- **Endereço de acesso:** https://account.mongodb.com/account/login
- **email de acesso:** green279@gmail.com
- **Senha:** raizen2024

#### Configuração do IP
- Após acessar o sistema vá no menu lateral esquerdo na parte de Network Access
![img.png](img.png)

- Selecione o botão ADD IP ADRESS
![img_1.png](img_1.png)

- Insira o ip da máquina que irá rodar o sistema
![img_2.png](img_2.png)


## Documentação da API

#### EndPoint de chamada

```http
  GET /api_url/get_weather/{city}
  ```
Recupera os dados da previsão do tempo para a cidade selecionada e salva os resultados na base de dados.
#### Retorno da Api
```json
{
    "city": "São Paulo",
    "message": "Previsão do tempo salva com sucesso!",
    "data": {
        "cod": "200",
        "message": 0,
        "cnt": 40,
        "list": [
            {
                "dt": 1704844800,
                "main": {
                    "temp": 23.53,
                    "feels_like": 23.77,
                    "temp_min": 23.53,
                    "temp_max": 26.35,
                    "pressure": 1015,
                    "sea_level": 1015,
                    "grnd_level": 929,
                    "humidity": 70,
                    "temp_kf": -2.82
                },
                "weather": [
                    {
                        "id": 500,
                        "main": "Rain",
                        "description": "light rain",
                        "icon": "10n"
                    }
                ],
                "clouds": {
                    "all": 75
                },
                "wind": {
                    "speed": 2.88,
                    "deg": 61,
                    "gust": 4.94
                },
                "visibility": 10000,
                "pop": 0.42,
                "rain": {
                    "3h": 0.22
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2024-01-10 00:00:00"
            }
            ],
                    "city": {
                        "id": 3448439,
                        "name": "São Paulo",
                        "coord": {
                            "lat": -23.5475,
                            "lon": -46.6361
                        },
                        "country": "BR",
                        "population": 10021295,
                        "timezone": -10800,
                        "sunrise": 1704788901,
                        "sunset": 1704837486
                    }
            }
}
  ```

```http
  GET /api_url/get_weather_database
  ```
Recupera os dados do historico de todas as previsões pesquisadas
#### Retorno da Api
```json
{
    "city": "São Paulo",
    "message": "Previsão do tempo salva com sucesso!",
    "data": {
        "cod": "200",
        "message": 0,
        "cnt": 40,
        "list": [
            {
                "dt": 1704844800,
                "main": {
                    "temp": 23.53,
                    "feels_like": 23.77,
                    "temp_min": 23.53,
                    "temp_max": 26.35,
                    "pressure": 1015,
                    "sea_level": 1015,
                    "grnd_level": 929,
                    "humidity": 70,
                    "temp_kf": -2.82
                },
                "weather": [
                    {
                        "id": 500,
                        "main": "Rain",
                        "description": "light rain",
                        "icon": "10n"
                    }
                ],
                "clouds": {
                    "all": 75
                },
                "wind": {
                    "speed": 2.88,
                    "deg": 61,
                    "gust": 4.94
                },
                "visibility": 10000,
                "pop": 0.42,
                "rain": {
                    "3h": 0.22
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2024-01-10 00:00:00"
            }
            ],
                    "city": {
                        "id": 3448439,
                        "name": "São Paulo",
                        "coord": {
                            "lat": -23.5475,
                            "lon": -46.6361
                        },
                        "country": "BR",
                        "population": 10021295,
                        "timezone": -10800,
                        "sunrise": 1704788901,
                        "sunset": 1704837486
                    }
            }
}
  ```


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`API_KEY=c99e7cccfcf2e5e618e757b0a8b8b04f`
`DATABASE_URL=mongodb+srv://raizen:raizen1234@cluster0.bzjws0s.mongodb.net/?retryWrites=true&w=majority`
`API_URL=http://api.openweathermap.org/data/2.5/forecast`


## Rodando via container

Clone o projeto

```bash
  git clone https://github.com/ridabe/weather-app-act
```

Entre no diretório do projeto

```bash
  cd my-project
```

Para construir a imagem Docker a partir do Dockerfile, no terminal, navegue até o diretório onde está localizado o Dockerfile e execute o comando:

```bash
  docker build -t minha-api .
```

Para executar um contêiner com a imagem criada:

```bash
  docker run -p 8000:8000 minha-api
```

Utilize o postman ou outro app para acessar as rotas da api, acesse o endereço iniciado pelo servidor:

```bash
  http://127.0.0.1:8000/get_weather/São Paulo
```
```bash
  http://127.0.0.1:8000/get_weather_database
```
** Dentro da pasta do projeto tera uma arquivo com as collections para serem usadas no postman ** 

## Melhorias Sugeridas

Melhorias propostas para a segunda versão:

- Refatorações;
- Melhorias de performance;
- Tratamento de erros(try);
- Testes Unitários;
- Ajustes de Typo.


## Suporte

Para suporte, mande um email para ridabe@uol.com.br ou entre em nosso whatsapp (11)94522-4263 (Ricardo Bene).


## Usado por

Esse projeto é parte do processo seletivo da:

- Raízen

![Logo](https://carreiras.raizen.com.br/wp-content/webp-express/webp-images/uploads/2022/03/logo_raizen.png.webp)

