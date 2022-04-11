"""
Создать класс Phone, у которого будут следующие атрибуты:
Определить атрибуты:
- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:
- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""
class Phone:

    def __init__(self, brand):
        self.brand = brand
        self.model = "model"
        self.issue_year = 1

    def get_info(self):
        print(f"{self.brand} {self.model} {self.issue_year}\n")

    def str(self):
        print(f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}\n\n")



phone1 = Phone("iPhone")
phone1.model = "13 Pro"
phone1.issue_year = 2021
phone1.get_info()
phone1.str()

phone2 = Phone("Samsung")
phone2.model = "21 lite"
phone2.issue_year = 2020
phone2.get_info()
phone2.str()
