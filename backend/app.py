from flask import Flask
import redis  # Импортируем библиотеку для работы с Redis

app = Flask(__name__)
redis_db = redis.Redis(host='redis', port=6379)  # Подключаемся к Redis

@app.route('/')
def hello():
    redis_db.incr('hits')  # Увеличиваем счетчик на 1
    return f'Эта страница открыта {redis_db.get("hits").decode()} раз!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5880)  # Запускаем сервер на порту 5880