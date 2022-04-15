# Nested List Comprehension

# matrix without list comprehension
matrix = []
for i in range(3):
    # Append 3 empty sublists to the empty list
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)

print("Without List Comprehension:", matrix)

# matrix with list comprehension
matrix = [[j for j in range(5)] for i in range(3)]

print("With List Comprehension:", matrix)
