"""
Пример программы для работы с ООП

Сделать
- класс User от класса Person
- добавить поле для пароля
- добавить метод проверки пароля
"""


class Person:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_info(self):
        print(f"{self.first_name} {self.last_name}, {self.age}")

    def say(self, content):
        print(f"<{self.first_name} {self.last_name}>: {content}")


class User(Person):
    password: str

    def check_password(self, user_password):
        return self.password == user_password


user = User("Nikita", "Mikhailov", 23)
user.print_info()
user.say("Hello")

user.password = "123456"
print(user.check_password("123456"))
