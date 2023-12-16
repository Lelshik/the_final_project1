# the_final_project1
Теоретический блок:
1. Ответы на 9 видео вопросов
2. Ответы на 10 писменных вопросов.
   
Практический блок 1:
Задание 1. Тестирование функциональности веб-приложения
Твоя задача — протестировать функциональность «Сделать заказ». Тесты на вёрстку напиши только для одного экрана. Подготовь их в виде чек-листа. Не забудь про кроссбраузерное тестирование. Баг-репорты оформи в YouTrack.
Задание 2. Ретест багов в мобильном приложении
Теперь возьмись за мобильное приложение. Разработчики исправили баги и отдали в тестирование. Тебе нужно провести ретест.
Задание 3. Регрессионное тестирование мобильного приложения по готовым тест-кейсам
Разработчики подготовили новую версию мобильного приложения. Перед релизом нужно провести регрессионное тестирование.
https://docs.google.com/document/d/1BOKjkTQWjdd6jwZ8ug8n2JJVWhtWficuf22BKkEKJ1g/edit?usp=sharing

Практический блок 2: Работа с базой данных
Задание 1. Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
SELECT cou.login, COUNT (*) AS "inDeliveryCount" FROM "Couriers" AS cou JOIN "Orders" AS ord ON cou.id = ord."courierId" WHERE ord."inDelivery" = true GROUP BY cou.login;
Задание 2. Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
1. SELECT track, cancelled, finished, "inDelivery" FROM "Orders";
2. SELECT track, CASE WHEN finished = true THEN '2' WHEN "inDelivery" = true THEN '1' WHEN cancelled = true THEN '-1' ELSE '0' END FROM "Orders";
Технические примечания:
Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.
Задание 3. Автоматизация теста к API
Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.
Технические примечания:
К проекту добавь файлы .gitignore и README.MD .
Логи лежат в файле error.log в папке /var/www/backend/logs.
configuration.py
URL_SERVICE = "https://10306dab-f44a-4b9c-9484-5f125d9a19d1.serverhub.praktikum-services.ru/"
CREATE_ORDER = "api/v1/orders"
REQUEST_ORDER = "/v1/orders/track?t"
data.py
order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
sender_stand_request.py
import configuration
import requests
import data

def post_create_order(order_body) :
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=order_body)
track_number = post_create_order(data.order_body).json()["track"]

response = post_create_order(data.order_body)
print(response.status_code)
print(response.json()["track"])

def get_order_on_number():
    track = post_create_order(data.order_body).json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.REQUEST_ORDER + str(track))


response  = get_order_on_number()
print(response.status_code)
test_order_by_number.py
import sender_stand_request
def positive_assert():
    order_response = sender_stand_request.get_order_on_number()
    assert order_response.status_code == 200

    def test_order_on_number_get_response_200():
        positive_assert()
