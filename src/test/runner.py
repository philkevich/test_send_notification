import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("API_URL")

if not url:
    raise ValueError("Ошибка: Переменная API_URL не найдена")

data = {"message": "тест"}

# Бесконечный цикл, чтобы сервис на Railway работал постоянно
while True:
    try:
        response = requests.post(url, json=data)
        print("Код ответа:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Ошибка запроса:", e)

    print("Ожидание 10 секунд...")
    time.sleep(10)
