# используем официальный образ Python 3.9
FROM python:3.9

# создаем директорию для приложения
WORKDIR /app

# копируем файлы приложения в Docker-контейнер
COPY . .

# устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# запуск тестов
CMD [ "pytest", "-v" ]
