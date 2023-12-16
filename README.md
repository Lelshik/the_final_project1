# the_final_project1
Теоретический блок:
1. Ответы на 9 видео вопросов
2. Ответы на 10 писменных вопросов.
   
Практический блок 1:
1. Тестирование функциональности веб-приложения
Твоя задача — протестировать функциональность «Сделать заказ». Тесты на вёрстку напиши только для одного экрана. Подготовь их в виде чек-листа. Не забудь про кроссбраузерное тестирование. Баг-репорты оформи в YouTrack.
2. Ретест багов в мобильном приложении
Теперь возьмись за мобильное приложение. Разработчики исправили баги и отдали в тестирование. Тебе нужно провести ретест.
3. Регрессионное тестирование мобильного приложения по готовым тест-кейсам
Разработчики подготовили новую версию мобильного приложения. Перед релизом нужно провести регрессионное тестирование.
https://docs.google.com/document/d/1BOKjkTQWjdd6jwZ8ug8n2JJVWhtWficuf22BKkEKJ1g/edit?usp=sharing 
Практический блок 2: Работа с базой данных
1. Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных. 
2. Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Технические примечания:
Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.
3. Автоматизация теста к API
Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.
Технические примечания:
К проекту добавь файлы .gitignore и README.MD .
Логи лежат в файле error.log в папке /var/www/backend/logs.
