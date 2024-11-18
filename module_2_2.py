first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and first == third:
    print('3 совпадения!=)')
elif first == second or second == third or first == third:
    print('2 совпадения!=)')
else:
    print('0 совпадений...=(')