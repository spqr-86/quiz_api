### Описание сервиса
REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}  
После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
Далее, полученные ответы сохраняется в базе данных. 
В случае, если в БД имеется такой же вопрос, к публичному API с викторинами выполняется дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.

### Начало работы

1. Склонируйте проект:


```git clone https://github.com/hlystovea/BBBS.git```  


2. Создайте файл .env по примеру env.example.


3. Запустите контейнеры:

```docker-compose up -d```

4. Запустите миграции:

```docker-compose run web alembic revision -m "Initial migration"```
```docker-compose run web alembic upgrade head"```
```docker-compose run web alembic revision --autogenerate -m "Initial migration""```

5. Документация будет доступна по адресу:
 
```http://localhost:8000/docs/```
