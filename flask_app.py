from flask import Flask, request, json
from config import *
import vk
import server
import vk_api
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    database_contents = ''
    connection = sqlite3.connect('/home/mcproger666/mysite/users.db')
    try:
        c = connection.cursor()
        rows = c.execute('SELECT DISTINCT * FROM users;')
        for row in rows:
            users_id, users_full_name, users_vk_id = row
            database_contents += '<p>{id}: {name}, {vk_id}</p>\n'.format(id=users_id, name=users_full_name,
                                                                         vk_id=users_vk_id)
        return '<h1>Database contents:</h1>' + database_contents
    finally:
        connection.close()
    return 'Smth wrong!'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        server.create_answer(data['object'], token)
        return 'ok'
