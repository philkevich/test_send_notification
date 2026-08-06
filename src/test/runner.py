import os
import requests
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Получаем URL из переменной окружения
url = os.getenv("API_URL")

if not url:
    raise ValueError("Ошибка: Переменная API_URL не найдена в файле .env")

data = {"message": "тест"}

try:
    response = requests.post(url, json=data)
    print("Код ответа:", response.status_code)
    print("Ответ сервера:", response.text)
except requests.exceptions.RequestException as e:
    print("Ошибка запроса:", e)