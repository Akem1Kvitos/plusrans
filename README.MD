Смотри postman collection для запросов
В кратце: 

В post/update в json кладём тело в котором ключи - названия колонок в базе

В delete/update необходимо прямо в рут указать id поля primary key таблицы с которой работаем

html, css, js файлы кладутся в **views** (читай местный readme)

**.env файл - в руте** 

* SERVICE_PORT=""
* SERVICE_WORKERS=""
* DB_HOST=""
* DB_USER=""
* DB_PASSWORD=""
* DB_NAME=""

Сборка и запуск

```
poetry install && poetry shell
python runner.py
```

Сервер запускается сразу в нескольких воркерах, в зависимости он настроект в .env

Енвы можно задавать любым способом


