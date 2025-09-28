import sqlite3


class StudentDB:
    def __init__(self, db_name="my_database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                first_name TEXT (100) NOT NULL,
                last_name TEXT (100) NOT NULL,
                grade INTEGER,
                subject TEXT
            )
        ''')
        self.conn.commit()


    # 1. CREATE
    def add_student(self, first_name, last_name, grade, subject):
        """Добавляет нового студента и возвращает его ID."""
        try:
            self.cursor.execute('''
                INSERT INTO students (first_name, last_name, grade, subject) 
                VALUES (?, ?, ?, ?)
            ''', (first_name, last_name, grade, subject))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении: {e}")
            return None

    # 2. READ
    def get_students(self):
        """Выводит список всех студентов."""
        self.cursor.execute('SELECT * FROM students')
        students = self.cursor.fetchall()

        print("\n--- Список студентов ---")
        if not students:
            print("Нет записей.")
            return

        header = f"{'ID':<4} {'Имя':<15} {'Фамилия':<15} {'Класс':<8} {'Предмет'}"
        print(header)
        print("-" * len(header))
        for s in students:
            print(f"{s[0]:<4} {s[1]:<15} {s[2]:<15} {s[3]:<8} {s[4]}")

    # 3. UPDATE
    def update_student(self, student_id, new_first_name, new_last_name):
        """Обновляет имя и фамилию студента по ID."""
        self.cursor.execute('''
            UPDATE students 
            SET first_name = ?, last_name = ?
            WHERE id = ?
        ''', (new_first_name, new_last_name, student_id))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"Студент ID {student_id} обновлен.")
        else:
            print(f"Студент ID {student_id} не найден для обновления.")

    # 4. DELETE
    def delete_student(self, student_id):
        """Удаляет студента по ID."""
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"Студент ID {student_id} удален.")
        else:
            print(f"Студент ID {student_id} не найден для удаления.")

    def close(self):
        self.conn.close()



def run_tests():
    db = StudentDB()
    print("База данных готова.")

    # 1. CREATE
    print("\n[C] Создание:")
    id_1 = db.add_student("Егор", "Давыдов", 8, "История")
    id_2 = db.add_student("Ольга", "Соловьева", 11, "Химия")
    db.add_student("Иван", "Петров", 10, "Геометрия")

    # 2. READ
    print("\n[R] Чтение после добавления:")
    db.get_students()

    # 3. UPDATE
    print("\n[U] Обновление:")
    if id_1:
        db.update_student(id_1, "Егор", "Давыденко")

    # READ после обновления
    print("\n[R] Чтение после обновления:")
    db.get_students()

    # 4. DELETE
    print("\n[D] Удаление:")
    if id_2:
        db.delete_student(id_2)

    # READ после удаления
    print("\n[R] Чтение после удаления:")
    db.get_students()

    db.close()
    print("\nТестирование завершено.")


if __name__ == "__main__":
    run_tests()