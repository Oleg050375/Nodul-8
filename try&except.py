def add_everything_up(a,b):
    try:
        return a + b  # сложение чисел в случае отсутствия ошибки
    except TypeError:
        if isinstance(a,int):  # проверка и преобразование первого аргумента
            a = str(a)
        if isinstance(b,int):  # проверка и преобразование второго аргумента
            b = str(b)
        return a + b  # конкатенация аргументов в итоговую строку

# ТЕСТ ----------------------------------------------------------------------------------------------------------------

print(add_everything_up(3,4))
print(add_everything_up('Din', 5))
print(add_everything_up(5, 'Sam'))
print(add_everything_up('Sam', 'Din'))