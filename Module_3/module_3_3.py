def print_params(a=1, b='сторка', c=True):
    print(a, b, c)

print('--- Пример 1 ---')
print_params()
print_params(4, 'новая строка')
print_params(True)
print_params(44, 55, False)
print_params('ещё одна строка')
print('')

print('--- Пример 2 ---')
print_params(b=25)
print_params(c=[1,2,3])
print('')

print('--- Пример 3 ---')
values_list = ['Тест', 3452.777, False]
values_dict = {'a': 'Тест 2', 'b': True, 'c': 348}
print_params(*values_list)
print_params(**values_dict)
print('')

print('--- Пример 4 ---')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
