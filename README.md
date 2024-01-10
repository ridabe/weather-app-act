
![Logo](https://carreiras.raizen.com.br/wp-content/webp-express/webp-images/uploads/2022/03/logo_raizen.png.webp)


# Raizen Teste

O desafio é Elaborar uma aplicação de backend utilizando a linguagem de programação Python que deverá conter 
uma API retornando os dados da previsão do tempo dos próximos dias. Para elaborar essa aplicação, 
utilizar a API de previsão do tempo de 5 dias do https://openweathermap.org/.


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
- sqlite3;
- dotenv.


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
[
    [
        1,
        "Jundiai",
        "{'cod': '200', 'message': 0, 'cnt': 40, 'list': [{'dt': 1704844800, 'main': {'temp': 23.46, 'feels_like': 23.98, 'temp_min': 21.74, 'temp_max': 23.46, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 930, 'humidity': 81, 'temp_kf': 1.72}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 57}, 'wind': {'speed': 2, 'deg': 94, 'gust': 2.76}, 'visibility': 10000, 'pop': 0.68, 'rain': {'3h': 1.66}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-01-10 00:00:00'}, {'dt': 1704855600, 'main': {'temp': 22.36, 'feels_like': 22.87, 'temp_min': 20.17, 'temp_max': 22.36, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 932, 'humidity': 85, 'temp_kf': 2.19}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 44}, 'wind': {'speed': 0.64, 'deg': 275, 'gust': 1.03}, 'visibility': 10000, 'pop': 0.52, 'rain': {'3h': 0.75}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-01-10 03:00:00'}, {'dt': 1704866400, 'main': {'temp': 20.76, 'feels_like': 21.22, 'temp_min': 19.41, 'temp_max': 20.76, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 930, 'humidity': 89, 'temp_kf': 1.35}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'clouds': {'all': 33}, 'wind': {'speed': 1.01, 'deg': 114, 'gust': 1.01}, 'visibility': 10000, 'pop': 0.51, 'sys': {'pod': 'n'}, 'dt_txt': '2024-01-10 06:00:00'}, {'dt': 1704877200, 'main': {'temp': 19.45, 'feels_like': 19.88, 'temp_min': 19.45, 'temp_max': 19.45, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 931, 'humidity': 93, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 69}, 'wind': }}",
        "2024-01-09 23:03:42"
    ]
]
  ```


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`API_KEY=c99e7cccfcf2e5e618e757b0a8b8b04f`
`DATABASE_URL=mongodb://user:password@localhost:27017/weather`
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

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/ridabe/weather-app-act
```

Entre no diretório do projeto

```bash
  cd my-project
```

Inicie o servidor com o comando

```bash
  uvicorn main:app --reload
```


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

- Raizen

![Logo](https://carreiras.raizen.com.br/wp-content/webp-express/webp-images/uploads/2022/03/logo_raizen.png.webp)

