#!/usr/bin/env python

from setuptools import setup, find_packages

djasa = __import__('djasa')

setup(name='Djasa',
      version=djasa.get_version(),
      description='A way to create a module in django like a module in python',
      author='Leonardo Orozco',
      author_email='leonardoorozcop@gmail.com',
      url='https://github.com/leonardoo/djasa/',
      packages = find_packages(exclude=['demo', 'demo.*']),	
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'],
     )