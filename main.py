import requests
from dotenv import dotenv_values
from fastapi import FastAPI
import sqlite3

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
        save_to_database(city, response.json())
        return {"city": city, "message": 'Previsão do tempo salva com sucesso!', "data": response.json()}
    else:
        return {"city": city, "message": 'Erro ao obter previsão do tempo.', "data": None}


# Função para criar o banco de dados SQLite e salvar histórico de chamadas
def save_to_database(city, response_data):
    conn = sqlite3.connect('weather_history.db') # # Melhorias proposta nesta parte, inserir estes dados da base no arquivo env
    cursor = conn.cursor()
   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            response_data TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Inserir dados na tabela
    cursor.execute('''
        INSERT INTO weather_history (city, response_data) VALUES (?, ?)
    ''', (city, str(response_data)))

    conn.commit()
    conn.close()


@app.get("/get_weather_database")
def get_weather_database():
    conn = sqlite3.connect('weather_history.db') # # Melhorias proposta nesta parte, inserir estes dados da base no arquivo env
    cursor = conn.cursor()
    # Recupera todos os dados da tabela
    cursor.execute("SELECT * FROM weather_history")
    return cursor.fetchall()
