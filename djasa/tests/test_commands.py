import os
import unittest

from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO

from .utils import remove_app, get_list_dir_files


class StartAppTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        app_name = "hello"
        call_command('startapp', app_name, stdout=out)
        self.assertIn('', out.getvalue())
        remove_app(app_name)

    def test_command_create_app(self):
        app_name = "base.apps.module1"
        call_command('startapp', app_name)
        modules = app_name.split(".")
        dirs = get_list_dir_files(modules[0])
        top_dir = os.getcwd()
        for i, path in enumerate(dirs):
            if i < len(modules):
                top_dir = os.path.join(top_dir, modules[i])
                self.assertEqual(path[0], top_dir)
                self.assertIn("__init__.py", path[1])
                if i == len(modules)-1:
                    self.assertIn("views.py", path[1])
                    self.assertIn("models.py", path[1])
                    self.assertIn("tests.py", path[1])
        remove_app(modules[0])

    @unittest.expectedFailure
    def test_command_with_multiples_dot(self):
        app_name = "base.apps..module1"
        error = False
        call_command('startapp', app_name)
        self.assertEqual(True, error)

    @unittest.expectedFailure
    def test_command_with_start_dot(self):
        app_name = ".base.apps.module1"
        error = False
        call_command('startapp', app_name)
        self.assertEqual(True, error)

    @unittest.expectedFailure
    def test_command_with_end_dot(self):
        app_name = "base.apps.module1."
        error = False
        call_command('startapp', app_name)
        self.assertEqual(True, error)

    def test_large_modules_create_app(self):
        modules = []
        app_module = "app"
        app_name = ""
        for i in range(5):
            modules.append(app_module)
        app_name = ".".join(modules)
        call_command('startapp', app_name)
        dirs = get_list_dir_files(modules[0])
        top_dir = os.getcwd()
        for i, path in enumerate(dirs):
            if i < len(modules):
                top_dir = os.path.join(top_dir, modules[i])
                self.assertEqual(path[0], top_dir)
                self.assertIn("__init__.py", path[1])
                if i == len(modules)-1:
                    self.assertIn("views.py", path[1])
                    self.assertIn("models.py", path[1])
                    self.assertIn("tests.py", path[1])
        remove_app(modules[0])
