# PythonLibPythonSnake — Web FrameWork написанный на python.

ККак использовать PS.
PS — имеет файл , config . Config — нужен для настройки вашего проекта.

version = 1.0
project_name = "PROJECT"
theme = "dark";
settings = { 'title' : "MySite"
, 'user_name' : "admin"
, 'user_password' : "123",}
version — отвечает за версию программы.

project_name — за название (В данном случае оно равно PROJECT)

theme — за тему css : есть два вида : dark , light

settings — массив содержащий не менее важные настройки , такие как:

title — название

user_name — за имя поьзователя в админке

user_password — за пароль.

ККак создать проект :
Для начала , запустите файл main.py , введите команду : help

Вы увидите :

["GET:user-name" , "GET:user-password" ,
               "GET:version" , "create-project" ,
               "start-project" , "help" ,
               "Release" , 'Error-Debug',
               "admin"]
Разберем команды:

GET:user-name — служит для получения имени пользователя из файла config

GET:user-password — служит для получения пароля пользователя из файла config

GET:version — служит для получения версии из файла config

сreate_project — создает проект

start-project — запускает проект

help — получение списка команд

Release- Пока не нужно

Error-Debug — узнать подробнее об ошибке

admin — перейти в админку

Теперь немного , о структуре папок

Папки:

admin — папка с панелью администратора

apps — папка с вашими шаблонами

config — папка с файлом конфигурации проекта

core — папка самого фреймворка

РРазберем наиболее важные папки
ППапка apps:
Папка содержит под папку templates (шаблоны), там находятся файлы index.html и about.html

Они служат для заготовки вашего сайта

Теперь запустив файл main.py вы сможете создать проект :

Вы увидит
Для того чтобы создать проект вам понадобится ввести команду start-project позже у вас высветится данные о том создался ли проект или нет.

если же нет , то вам высветится ошибка с кодом , а код ошибки можно ввести в команду Error-Debug и получить Информацию об ошибке . после того как вы создали проект перейдите в админку.

Список команд админки

admin_comands = [
'Create','add-paragraph' , ' add-caption' , 'add-field' , 'add-button:into-field'
]
Create — нужна для завершения проекта , тогда когда он уже готов

add-paragraph — Нужна для создания параграфа на сайте

add-caption — Нужна для создания заголовка на сайте

add-field — Нужна для создания формы

add-button:into-field - пока не работает
