## Установка

    Установить в plp:
    pip install -e git+https://github.com/miptliot/plp-extension-helloworld.git@master#egg=plp_hello_world
    Добавить в файле настроек plp:
    INSTALLED_APPS += ('plp_hello_world', )
    Добавить в urls.py:
    urlpatterns += patterns('',
        url(r"", include("plp_hello_world.urls")),
    )
    Запустить миграции ./manage.py migrate

## Работа с приложением

    pip install с флагом -e установит все как обычный git репозиторий в директорию:
    <путь к virtualenv директории>/src/plp-hello-world

    Действия, описанные далее, добавляют/изменяют файлы в этой директории

    #### Создание миграций

    Для создания миграций после изменения/добавления моделей в plp-extension-helloworld запустить в plp:
    ./manage.py makemigrations plp_hello_world

    #### Работа с файлами переводов

    В файле настроек plp добавить в LOCALE_PATHS путь к директории locale в установленном приложении,
    например: '/home/user/python/npoed-plp-edx/npoed_plp/venv/src/plp-hello-world/plp_hello_world/locale'
    Запустить ./manage.py makemessages -l ru -e html -e py --no-location
    откатить изменения в файле переводов plp: git checkout -- locale/ru/LC_MESSAGES/django.po
    Скомпилировать переводы: ./manage.py compilemessages
    Убрать добавленный путь в LOCALE_PATHS
