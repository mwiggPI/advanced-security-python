import os
import sqlite3

from flask import Flask


ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TEMPLATES = os.path.join(ROOT, 'templates')
STRIPESECRET = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
flaskapp = Flask("BookStore", template_folder=TEMPLATES)
flaskapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database_uri = os.environ.get('SQLITE_URI', ':memory:')

database = sqlite3.connect(database_uri, check_same_thread=False)
cursor = database.cursor()
