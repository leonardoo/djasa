#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'djasa.runtests.settings'

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    if django.VERSION >= (1, 7, 0):
        # starting from 1.7.0 we need to run setup() in order to populate
        # app config
        django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["djasa"])
    sys.exit(failures)
