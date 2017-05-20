import sqlite3


def add_into_db(user_info):
    full_name = user_info['first_name'] + ' ' + user_info['last_name']
    uid = user_info['id']
    connection = sqlite3.connect('/home/mcproger666/mysite/users.db')
    try:
        c = connection.cursor()
        c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", (None, full_name, uid))
        connection.commit()
    finally:
        connection.close()


def get_db_id(user_id):
    connection = sqlite3.connect('/home/mcproger666/mysite/users.db')
    try:
        c = connection.cursor()
        c.execute("SELECT * FROM users WHERE vk_id = ?", (user_id,))
        user_info = c.fetchone()
    finally:
        connection.close()
    db_id, full_name, vk_id = user_info
    return db_id
