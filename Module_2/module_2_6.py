import random


def check(i, j):
    conditions = [a % (i + j) == 0, i != j, not f'{i}+{j}' in b, not f'{j}+{i}' in b]
    return conditions


a = random.choice(range(3, 20 + 1))
b = []

for num_1 in range(1, a):
    for num_2 in range(1, a):
        if all(check(num_1, num_2)):
            b.append(f'{num_1}+{num_2}')

print(f'Число: {a}')
print(f'Пароль: {''.join(b).replace('+', '')}')
