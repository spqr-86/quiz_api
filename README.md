# Описание сервиса
REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}  ;

После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.


# Информация по запросам
1. Склонируйте репозиторий
2. Выполните в терминале docker-compose build
3. 
4. Перейдите на http://localhost:8000/docs/

### Начало работы

1. Склонируйте проект:


```git clone https://github.com/hlystovea/BBBS.git```  

2. Запустите контейнеры:

```docker-compose up -d```

Frontend подтянется из docker-hub. 

4. Запустите миграции:

```docker-compose exec backend python manage.py migrate --noinput```

5. Соберите статику:

```docker-compose exec backend python manage.py collectstatic --no-input```

6. Создайте своего суперпользователя:

```docker-compose exec backend python manage.py createsuperuser```

7. Сайт будет доступен по адресу:
 
```http://127.0.0.1```
