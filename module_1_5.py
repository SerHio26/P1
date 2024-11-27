
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matr = []
        for j in range(m):
            matr.append(value)
        matrix.append(matr)
    return matrix

results_1 = get_matrix(2, 3, 10)
results_2 = get_matrix(5, 6, 15)
results_3 = get_matrix(3, 6, 8)

print(results_1)
print(results_2)
print(results_3)