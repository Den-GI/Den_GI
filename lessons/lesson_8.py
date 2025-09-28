import sqlite3

connect = sqlite3.connect('users_grades.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCHAR(50) NOT NULL,
        grade INTEGER NOT NULL,
        userid INTEGER,
        FOREIGN KEY (userid) REFERENCES users(user_id)
    )
''')

def add_user(name_1, age):
    # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    cursor.execute(
        "INSERT INTO users(name, age) VALUES (?,?)",
        (name_1, age)
    )
    connect.commit()
    print('Пользователь добавлен!!')

# add_user("Ardager", 26)
# add_user("Oleg", 20)
# add_user("Alex", 25)

def add_grade(subject, grade, userid):
    cursor.execute(
        "INSERT INTO grades(subject, grade, userid) VALUES (?,?,?)",
        (subject, grade, userid)
    )
    connect.commit()
    print('Оценка добавлена!!')

# add_grade("Алгебра", 5, 99)


def get_users_grades():
    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade
        FROM users FULL OUTER JOIN grades ON users.user_id = grades.userid
    ''')

    users = cursor.fetchall()

    for i in users:
        print(f"name: {i[0]}, subject: {i[1]}, grade: {i[2]}")

get_users_grades()
