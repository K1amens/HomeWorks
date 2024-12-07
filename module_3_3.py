def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print('1.Функция с параметрами по умолчанию:\n')

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print('\n-------Запомни-------\n')

print('2.Распаковка параметров:\n')

values_list = [1, 'Hello', False]
values_dict = {'a': 2, 'b': 'Hi', 'c': True}

print_params(*values_list)
print_params(**values_dict)

print('\n-------а то забудешь-------\n')

print('3.Распаковка + отдельные параметры:\n')

values_list_2 = [45.25, 'String']

print_params(*values_list_2, 42)

print('\n-------Jason Statham-------')