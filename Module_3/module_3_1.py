import os

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), str.upper(string), str.lower(string))


def is_contains(string, list_to_search):
    count_calls()
    string = str.lower(string)
    for i in range(len(list_to_search)):
        list_to_search[i] = str.lower(list_to_search[i])
    if string in list_to_search:
        return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

# stop = ''
# while stop != 'n':
#     os.system('cls')
#     text1 = input('Введите строку (для выхода введите exit): ')
#     if text1 == 'exit':
#         break
#     text2 = input('Введите произвольные строки через запятую с пробелом: ')
#     print(string_info(text1))
#     print(is_contains(text1, text2.split(', ')))
#     print(calls)
#     stop = str(input('Продолжить? (y/n): '))
