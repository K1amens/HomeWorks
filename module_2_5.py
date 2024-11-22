def get_matrix(n, m , value):
    matrix = []


    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)


    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)


print(f"Результат 1:"
      f"\n{result1}")
print(f"Результат 2:"
      f"\n{result2}")
print(f"Результат 3:"
      f"\n{result3}")