class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        plov = "высшее оброзования True" if self.higher_education else "высшее оброзования False"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}. "
              f"Моя профессия - {self.occupation}, и у меня - {plov}.")

chel1 = Person("Kamino", "08.04.2000", "архитектор", True)
chel2 = Person("Simon", "06.06.2006", "спасатель",  True)
chel3 = Person("Isken", "15.10.2011", "програмист", False)



chel1.introduce()
chel2.introduce()
chel3.introduce()

