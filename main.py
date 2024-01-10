import requests
from dotenv import dotenv_values
from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

env_vars = dotenv_values(".env")
API_KEY = env_vars.get("API_KEY")
DB_URL = env_vars.get("DATABASE_URL")
BASE_URL = env_vars.get("API_URL")


@app.get("/get_weather/{city}")
# Função para buscar previsão do tempo
def get_weather_forecast(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',  # Pode ser 'imperial' para Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.ok:
        save_to_mongodb(city, response.json())
        return {"city": city, "message": 'Previsão do tempo salva com sucesso!', "data": response.json()}
    else:
        return {"city": city, "message": 'Erro ao obter previsão do tempo.', "data": None}


def save_to_mongodb(city, response_data):
    client = MongoClient(DB_URL)

    db = client['raizen']
    collection = db['weather']

    # Inserindo dados
    entry = {
        'city': city,
        'response_data': response_data,
        'timestamp': datetime.now()
    }
    collection.insert_one(entry)
    client.close()


@app.get("/get_weather_database")
def get_weather_database():
    client = MongoClient(DB_URL)

    db = client['raizen']
    collection = db['weather']
    # Consulta para recuperar todos os documentos da coleção
    result = collection.find({})
    data = []
    for doc in result:
        if '_id' in doc:
            doc.pop('_id')
        data.append(doc)

    return data
