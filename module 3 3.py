# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True): #Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
    print(a, b, c) # Функция должна выводить эти параметры.


print_params(a=6, b=6, c=6) # Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(a=6, b=6)
print_params(c=6)
print_params()
print_params(b=25) # Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(c = [1,2,3])

# 2.Распаковка параметров:
values_list = [1, 'строка', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = ['a', 1]
print_params(*values_list_2, 42)
