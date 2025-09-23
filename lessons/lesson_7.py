import sqlite3

# A4
connect = sqlite3.connect("users.db")

# Рука с ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE If NOT EXISTS users(
    name VARCAHR (100) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
''')
connect.commit()


# def add_user(name, age, hobby):
#     # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES ("{name}", "{age}", "{hobby}")')
#     cursor.execute(
#         'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
#         (name, age, hobby)
#     )
#     connect.commit()
#     print('ползователь добавлен')


#
# add_user('isek', 52, 'wrestler')


def get_users():
    cursor.execute('SELECT name,age,hobby FROM users')
    users = cursor.fetchall()
    # users = cursor.fetchmany(10)
    # users = cursor.fetchone()
    for user in users:
        print(f'user: {user[0]}, age: {user[1]}, hobby: {user[2]}')


get_users()


def update_user(row_id, name=None, age=None, hobby=None):
    if name:
        cursor.execute(
            'UPDATE users SET name = ? WHERE rowid = ? ',
            (name, row_id)
        )
    elif age:
        cursor.execute(
            'UPDATE users SET age = ? WHERE rowid = ? ',
            (name, row_id)
        )
    elif hobby:
        cursor.execute(
            'UPDATE users SET hobby = ? WHERE rowid = ? ',
            (name, row_id)
        )
    else:
        print('ничо')
    connect.commit()
    print('пользователь обновлен')


update_user('isek', 5)

def delete_user(row_id):
    cursor.execute(
        'DELETE FROM users WHERE rowid = "{row_id}"',
    )
    connect.commit()


delete_user(1)