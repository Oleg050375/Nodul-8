class Car:  # класс автомобилей
    def __init__(self, model, VIN, numbers):
        self.is_valid_vin(VIN)  # проверка VIN при создании объекта
        self.is_valid_mumbers(numbers)  # проверка номера при создании объекта
        self.model = model  # название модели (str)
        self.__VIN = VIN  # VIN-номер автомобиля (int) защищённый от переопределения
        self.__numbers = numbers  # номера автомобиля (str) защищённый от переопределения
    def is_valid_vin(self, VIN):  # метод проверки VIN
        if not isinstance(VIN, int):  # проверка типа данных VIN
            raise IncorrectVinNumber('Некорректный тип VIN номера')  # генерация ошибки типа данных VIN
        if VIN < 1000000 or VIN > 9999999:  # проверка диапазона VIN
            raise IncorrectVinNumber('Неверный диапазон для VIN номера')  # генерация ошибки диапазона VIN
        return True
    def is_valid_mumbers(self, numbers):  # метод проверки номера
        if not isinstance(numbers, str):  # проверка типа данных номера
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')  # генерация ошибки типа данных номера
        if not len(numbers) == 6:  # проверка длины номера
            raise IncorrectCarNumbers('Неверная длина номера')  # генерация ошибки длины номера
        return True

class IncorrectVinNumber(Exception):  # класс ошибки проверки VIN
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):  # класс ошибки проверки номера
    def __init__(self, message):
        self.message = message

# ТЕСТ ---------------------------------------------------------------------------------------------------------------

try:
    z = Car('Zeekr', 7777777, 'a1b2c3')
except IncorrectVinNumber as exc:
    print(exc.message)
    #print(z._Car__VIN)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{z.model} успешно создан')

try:
    a = Car('Avatr', 666, 'a4b5c6')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{a.model} успешно создан')

try:
    b = Car('BYD', 5555555, 'a7b8c')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{b.model} успешно создан')

print(z)  # взглянем на объект z
#print(a)  # взглянем на объект a
#print(b)  # взглянем на объект b