
# проект api-yatube
## Описание: 

Даный проект - это социальная сеть для авторов и их поклонников, с доступом через api интерфейс.
Она основана на Django REST framework и использует аутентификацию по JWT + Djoser.
Предоставляемые возможности api интерфейса для пользователей соц сети: 
просмотр, добавление и редактирование постов, просмотр групп, подписка на авторов постов,
также присутствует возможность добавления комментариев к постам.

-------------
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке
`
git clone https://github.com/yandex-praktikum/kittygram_backend.git
`

Перейти в каталог kittygram_backend
`
cd kittygram_backend
`

Cоздать и активировать виртуальное окружение
`
python3 -m venv env
`

* Если у вас Linux/macOS
    `
    source env/bin/activate
    `

* Если у вас windows
    `
    source env/scripts/activate
    `

Обновить pip
`
python3 -m pip install --upgrade pip
`

Установить зависимости из файла requirements.txt
`
pip install -r requirements.txt
`

Выполнить миграции
`
python3 manage.py migrate
`

Запустить проект
`
python3 manage.py runserver
`

-------------
## Примеры работы с api:

## создать пост:

 POST запрос к api:
`http://127.0.0.1:8000/api/v1/posts/`
`{
    "text": "Обязательное поле."
}`

ответ api:
`{
    "id": 12,
    "author": "user",
    "text": "Обязательное поле.",
    "pub_date": "2022-12-12T17:06:27.819262Z",
    "image": null,
    "group": null
}`

## создать пост:

 POST запрос к api: `http://127.0.0.1:8000/api/v1/posts/`
`{
    "text": "Обязательное поле."
}`

ответ api:
`{
    "id": 12,
    "author": "user",
    "text": "Обязательное поле.",
    "pub_date": "2022-12-12T17:06:27.819262Z",
    "image": null,
    "group": null
}`

## удалить пост:

 DEL  запрос к api: `http://127.0.0.1:8000/api/v1/posts/12/`

## подписатся на автора:
 POST запрос к api: `http://127.0.0.1:8000/api/v1/follow/`
`{
    "following": "uss"
}`

ответ api:
`{
    "id": 15,
    "following": "uss",
    "user": "user"
`}

### Автор проекта
    Сергей Долгов

