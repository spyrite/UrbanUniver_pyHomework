# Максимум в списке

def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i

    return max_


print(find_max([1, 5, 1, 2, 0]))


# Подсчёт четных чисел в списке

def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1

    return counter


print(count_even([1, 2, 3, 5, 33, 2, 3, 2, 0]))


# Уникальный список

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(unique([33, 33, 22, 11, 33, 11, 99, 99]))
