def calculate_structure_sum(data):
    summ = 0

    for i in range(len(data)):
        match data[i]:
            case list():
                summ += calculate_structure_sum(data[i])
            case tuple():
                summ += calculate_structure_sum(data[i])
            case set():
                summ += calculate_structure_sum(list(data[i]))
            case dict():
                summ += calculate_structure_sum(list(dict(data[i]).keys()))
                summ += calculate_structure_sum(list(dict(data[i]).values()))
            case int():
                summ += data[i]
            case str():
                summ += len(data[i])

    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
