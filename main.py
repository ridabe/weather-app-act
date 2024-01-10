import requests
from dotenv import dotenv_values
from fastapi import FastAPI
import sqlite3
from pymongo import MongoClient
import pymongo
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
    # client = pymongo.MongoClient("mongodb://localhost:27017/")  # Conectando ao MongoDB localmente
    client = MongoClient(
        'mongodb+srv://recrud:recrud2023bne@recrudprd.b82su.mongodb.net/recrud?retryWrites=true&w=majority')

    db = client['recrud']
    collection = db['weather']
    # db = client['weather_history']
    # collection = db['weather']

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
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    client = MongoClient(
        'mongodb+srv://recrud:recrud2023bne@recrudprd.b82su.mongodb.net/recrud?retryWrites=true&w=majority')

    db = client['recrud']
    collection = db['weather']

    # # Selecionando o banco de dados
    # db = client["weather_history"]
    #
    # # Selecionando a coleção
    # collection = db["weather"]

    # Consulta para recuperar todos os documentos da coleção
    result = collection.find({})
    return result
