Djasa
=====

Django Another Start App(djasa) modify the way to create a new app in django, 
you do not have to create an app and move from the current directory, 
only send the app's name like a module in python core.apps.module1

Installation
------------

To install it, simply: ::

    pip install djasa

## Add it to your Django Project

INSTALLED_APPS on settings.py

    INSTALLED_APPS = (
        ...
        'djasa',
        ...
    )

example run:

python manage.py startapp base.apps.module