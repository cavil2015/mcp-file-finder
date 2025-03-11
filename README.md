# MCP File Finder

## Описание

MCP сервер для поиска файлов по фрагменту пути.

## 📦 Установка

1. Убедитесь, что установлен Python 3.8+
2. Клонируйте репозиторий:

git clone https://github.com/cavil2015/mcp-file-finder.git cd mcp-file-finder

3. Установите зависимости:

pip install -r requirements.txt

## 🚀 Запуск сервера

python mcp_server.py

Сервер будет запущен по адресу:

http://127.0.0.1:5000

## 🔍 Примеры запросов

- Найти все файлы, содержащие "test":

http://127.0.0.1:5000/find?query=test&dir=.

- Пример ответа(json):
  [
  {
  "name": "testfile.txt",
  "path": "/home/user/projects/testfile.txt",
  "size": 1024,
  "created_at": "Tue Mar 11 12:34:56 2025"
  }
  ]
