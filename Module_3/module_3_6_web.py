def calc(data):
    summa = 0
    for elem in data:
        if isinstance(elem, (int,float)):
            summa += elem
        elif isinstance(elem,str):
            summa += len(elem)
        elif isinstance(elem, (list,tuple,set)):
            summa += calc(elem)
        elif isinstance(elem, dict):
            summa += calc(elem.items())
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': [3,[4,2]], 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calc(data_structure))


