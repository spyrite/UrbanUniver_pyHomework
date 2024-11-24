my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    number = my_list[i]
    i = i + 1
    if number > 0:
        print(number)
        continue
    if number < 0:
        break