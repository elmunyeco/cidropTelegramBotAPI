#!/usr/bin/env python
from setuptools import setup
from io import open
import re

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

with open('telebot/version.py', 'r', encoding='utf-8') as f:  # Credits: LonamiWebs
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$",
                        f.read(), flags=re.MULTILINE).group(1)

setup(name='cidropBotAPI',
      version=version,
      description='Consultorio Dr. Omar Prieto Telegram bot api. ',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      author='elmunyeco',
      author_email='elyecomun@gmail.com',
      url='https://github.com/elmunyeco/cidropTelegramBotAPI',
      packages=['telebot'],
      keywords='telegram bot api tools cardiologia integral dr. omar prieto',
      install_requires=['requests'],
      extras_require={
          'json': 'ujson',
          'redis': 'redis>=3.4.1'
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
      ]
      )