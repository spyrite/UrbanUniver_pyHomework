def get_matrix(n, m, value):
    matrix = list((list(value for j in range(m))) for i in range(n))
    return matrix

results = [get_matrix(2, 2, 10), get_matrix(3, 5, 42), get_matrix(4, 2, 13)]
for result in results:
    print(result)
