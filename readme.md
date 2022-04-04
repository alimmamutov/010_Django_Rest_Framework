# Django REST framework
## Мамутов Алим 
***

**Урок 1. Введение в REST и Django REST Framework**

***Практическое задание***

На протяжении всего курса в практическом задании мы по частям будем разрабатывать проект
«Web-сервис для работы с TODO-заметками». Вот примерное описание работы всего сайта.
На сайте будет 3 категории пользователей: администраторы, менеджеры проектов и разработчики.
Сайт позволяет работать с TODO-заметками, которые относятся к какому-либо проекту. Можно
добавить на сайт проект и затем сохранять по нему заметки, содержащие текст и статус. Одним
проектом занимается команда разработчиков и менеджеров.
    
***После каждого занятия:***
   
● сразу будем применять полученные знания на практике;

● добавлять в проект новые опции, относящийся к теме занятия.

В первом практическом задании создадим пользователя и API для работы с ним.

***В самостоятельной работе отработаем умения***

● подключать DRF к проекту;

● создавать REST API для простой модели данных.

***Зачем?***

Для использования базовых классов DRF в дальнейших проектах.

***Последовательность действий***
1. Создать новый проект на github или gitlab.
2. Создать django-проект.
3. Установить DRF и подключить его к django-проекту.
4. Создать приложение для работы с пользователем.
5. Создать свою модель пользователя.
6. В ней поле email сделать уникальным.
7. Сделать для неё базовое API — по аналогии модели Author. В качестве полей выбрать
username, firstname, lastname, email. Если выбрать все поля, при попытке сериализации может
возникнуть ошибка сериализации связанного поля. Эту тему мы рассмотрим далее.
8. Подключить стандартную админку.
9. Создать суперпользователя.
10. (Задание со *) Создать management command — скрипт для запуска через manage.py для
автоматического создания суперпользователя и нескольких тестовых пользователей
(Management commands).
11. Сдать работу в виде ссылки на репозиторий с кодом.
***
**Урок 2. Введение в REST и Django REST Framework**

***Практическое задание***

У нас есть API для работы с пользователями. Теперь необходимо создать для него интерфейс на
React.
В этой самостоятельной работе мы тренируем умения

● создавать приложение на React;

● использовать компонентный подход;

● настраивать взаимодействие back-end и front-end;

● применять One Way Data Flow.

***Зачем?***

Для создания front-end-части приложений на React.

***Последовательность действий***
1. С помощью create-react-app создать приложение для front-end-части проекта.
2. На React создать страницу для отображения списка пользователей из нескольких
компонентов. Пока эта страница будет доступна всем, после разграничения прав и только
для администратора.
3. Добавить на страницу компоненты Menu и Footer.
4. В главном приложении получить данные обо всех пользователях и вывести их на странице.
***
***
****Служебное****

*Создание виртуального окружения*

      python -m venv venv

*Для установки нужного venv:*
    
      pip install -r requirements.txt     
      (requirements.txt лежит в корне проекта)

*Для выгрузки venv:*

      pip freeze > requirements.txt

*Для очистки venv:*

      pip uninstall -r requirements.txt

***Для передачи файлов по SSH***

*На сервер:*

      pscp -P 22 “C:\files or docs\filename” root@178.21.11.180:/home/django/09_Django_2_optimization_tools/

*С сервера:*

      pscp -P 22 root@178.21.11.180:/home/django/09_Django_2_optimization_tools/ C:\Users\Алим\Desktop\Geek\009_Django_Optim_Tools
***

