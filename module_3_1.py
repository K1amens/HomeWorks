calls = 0


def count_calls(calls):
    print(calls)


def string_info(string):
    global calls
    calls += 1
    tuple_ = len(string), string.upper(), string.lower()
    return tuple_


def is_contains(string, list_):
    global calls
    calls += 1
    for item in list_:
        list_two = []
        list_two.append(item.lower())
    if string.lower() in list_two:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)