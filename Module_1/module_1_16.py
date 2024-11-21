
immutable_var = (10, 20, 30, True, 'Text', 5.5)
print('Immutable tuple:', immutable_var)

#immutable_var[2] = 555 - не работает,
#так как кортежи являются неизменяемыми коллекциями и такое действие не поддежривают

mutable_list = [10, 20, 30, True, 'Text', 5.5]
mutable_list[3] = False
mutable_list[5] = 'New value'
print('Mutable list:', mutable_list)
