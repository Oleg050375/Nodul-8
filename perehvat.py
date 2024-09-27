def personal_sum(numbers):
    result = 0  # переменная результата
    incorrect_data = 0  # счётчик исключений
    try:
        for i in numbers:  # перебор элементов коллекции
            try:
                result += i
            except TypeError:  # обработка ошибки типа данных
                incorrect_data += 1
    except:  # обработка ошибки ввода не коллекции
        return 'В numbers записан некорректный тип данных'
    else:  # возврат результата обработки коллекции
        return (result, incorrect_data)

def calculate_average(numbers):
    try:
        return personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1])  # вычисление среднего
    except ZeroDivisionError:  # обработка ошибки деления на ноль
        return 0
    except TypeError:  # обработка ошибки типа данных
        print('В numbers записан некорректный тип данных')

# ТЕСТ ----------------------------------------------------------------------------------------------------------------

#print(personal_sum([1,2,3]))
#print(personal_sum(345))
#print(personal_sum('789'))
#print(personal_sum([1,'2',5,'7']))

print(calculate_average([1,2,3]))
print(calculate_average(345))
print(calculate_average('789'))
print(calculate_average([1,'2',5,'7']))