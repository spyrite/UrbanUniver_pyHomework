from fake_math import divide as div0
from true_math import divide as div1

results = [
    div0(45, 5),
    div0(33, 0),
    div1(94, 3),
    div1(23, 0)
]

print('\n'.join(str(result) for result in results))