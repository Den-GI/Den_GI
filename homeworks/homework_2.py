class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"меня зовут: {self.name}, я родился: {self.birth_date}, я работаю: {self.occupation}, высшее образавания: {self.higher_education} ")


class Classmate(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник Данияра, я родился {self.birth_date}, я работаю {self.occupation},  высшее образавания: {self.higher_education} ")

class Friend(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name},я друг Данияра, я родился {self.birth_date}, я работаю {self.occupation},  высшее образавания: {self.higher_education} ")


pivo1 = Classmate(name="Акжол", birth_date="12.04.2004", occupation="Тренером", higher_education=False )
pivo1.introduce()
pivo2 = Classmate(name="Жоломан", birth_date="07.10.2004", occupation="Минестерстве", higher_education=True)
pivo2.introduce()
vodka1 = Friend(name="Кусака", birth_date="13.06.2003", occupation="Дизайнером", higher_education=False)
vodka1.introduce()
vodka2 = Friend(name="Фумита", birth_date="06.06.2004", occupation="Директором", higher_education=True)
vodka2.introduce()

print("Данияр это я, я родился 08.04.2011, я работаю программистом ")




