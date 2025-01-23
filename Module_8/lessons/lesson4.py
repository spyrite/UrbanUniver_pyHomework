# def greet_person(person_name):
#     if person_name == 'ВоланДеМорт':
#         raise Exception(f'Мы не любим тебя, {person_name}')
#     print(f'Привет, {person_name}!')
#
# greet_person('Дорогой ученик')
# greet_person('ВоланДеМорт')


# try:
#     raise NameError('Привет Там')
# except NameError as exc:
#     print(f'Исключение типа {type(exc)} пролетело мимо, аргументы: {exc.args}')
#     raise


class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def f(a, b):
    if b == 0:
        raise ProZero('Деление на нуль невозможно', {'a': a, 'b': b})
    return a / b

try:
    result = f(10, 0)
    print(result)
except ProZero as exc:
    print('Не очень хороший день, мы словили ошибку.')
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Дополнительная информация {exc.extra_info}')


print(f(5, 0))
