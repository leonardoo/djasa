import errno
import re
import os
from os import path
from importlib import import_module

import django
from django.core.management.base import CommandError
from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = ("Creates a Django app directory structure for the given app "
            "name in the current directory")

    def handle(self, app_name=None, **options):
        self._validate_name(app_name, "app")    
        array = app_name.split(".")
        app_name = array[-1]
        #this method only exits in version >= django 1.6
        if django.VERSION >= (1, 6, 0):
            self.validate_name(app_name, "app")

        # Check that the app_name cannot be imported.
        try:
            import_module(app_name)
        except ImportError:
            pass
        else:
            raise CommandError("%r conflicts with the name of an existing "
                               "Python module and cannot be used as an app "
                               "name. Please try another name." % app_name)
        top_dir = os.getcwd()
        enum = enumerate(array)
        last_index = list(enum)[-1][0]
        for i,name in enumerate(array):
            top_dir = path.join(top_dir, name)
            try:
                os.makedirs(top_dir)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    message = e
                    raise CommandError(message)
            if i != last_index:
                name_file = "__init__.py"
                if not "__init__.py" in os.listdir(top_dir):
                    open(path.join(top_dir, name_file), 'a').close()

        super(Command, self).handle('app', app_name, os.sep.join(array), **options)
        #super(Command, self).handle('app', app_name, target, **options)


    def _validate_name(self, name, app_or_project):
        if name is None:
            raise CommandError("you must provide %s %s name" % (
                "an" if app_or_project == "app" else "a", app_or_project))
        # If it's not a valid directory name.

        if not re.search(r'^(?!\.)', name):
            message = 'make sure the name do not begins with a point'
            raise CommandError("%r is not a valid %s name. Please %s." %
                               (name, app_or_project, message))
        elif not re.search(r'^.*[_a-zA-Z0-9]$', name):
            message = 'make sure the name do not ends with a point'
            raise CommandError("%r is not a valid %s name. Please %s." %
                               (name, app_or_project, message))
        elif  not re.search(r'^([_a-zA-Z0-9]+(\.(?!\.+)))*[_a-zA-Z0-9]+$', name):
            message = 'make sure the name has only one point between the modules'
            raise CommandError("%r is not a valid %s name. Please %s." %
                               (name, app_or_project, message))

        
        if not re.search(r'^([_a-zA-Z]\w*|\.)*$', name):
            
            # Provide a smart error message, depending on the error.
            if not re.search(r'^[_a-zA-Z]', name):
                
                message = 'make sure the name begins with a letter or underscore'
            else:
                
                message = 'use only numbers, letters, points and underscores'
            raise CommandError("%r is not a valid %s name. Please %s." %
                               (name, app_or_project, message))