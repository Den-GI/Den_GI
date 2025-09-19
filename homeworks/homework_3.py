class Person:
    def _init_(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self._occupation = occupation
        self._higher_education = higher_education

    @property
    def occupation(self):
        return self._occupation

    @property
    def higher_education(self):
        return self._higher_education

    def introduce(self):
        education_status = "есть" if self.higher_education else "нет"
        print( f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. У меня {education_status} высшего образования.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education,group):
        super()._init_(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        education_status = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Я учился с Игорем в группе {self.group}. У меня {education_status} высшего образования.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super()._init_(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_status = "есть" if self.higher_education else "нет"
        print(
            f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Мое хобби {self.hobby}. У меня {education_status} высшего образования.")


# Примеры как в вашем коде
pivo1 = Classmate(name="Акжол", birth_date="12.04.2004", occupation="Тренер", group="110", higher_education=False)
pivo1.introduce()

pivo2 = Classmate(name="Жоломан", birth_date="07.10.2004", occupation="Минестерсто", group="110", higher_education=True)
pivo2.introduce()

vodka1 = Friend(name="Кусака", birth_date="13.06.2003", occupation="Дизайнер", hobby="рисование", higher_education=False)
vodka1.introduce()

vodka2 = Friend(name="Фумита", birth_date="06.06.2004", occupation="Директор",hobby="спорт", higher_education=True)
vodka2.introduce()

print("Данияр это я, я родился 08.04.2011, я борец")