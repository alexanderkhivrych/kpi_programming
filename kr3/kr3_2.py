from random import *


def int_num(prompt):
    num = input(prompt)
    try:
        if int(num):
            return int(num)
    except ValueError:
        print("Error, you must enter a number")
        return int_num(prompt)


m = int_num("Enter m:")
n = int_num("Enter n:")

matrix = []
pair_number_count = 0
not_pair_number_count = 0

for i in range(m):
    row = []
    for j in range(n):
        row.append(randint(0, 99))
    matrix.append(row)

for row in matrix:
    for col in row:
        if col % 2:
            pair_number_count += 1
        else:
            not_pair_number_count += 1

print('matrix = {0}\npair numbers count = {1}\nnot a pair numbers count = {2}'
      .format(matrix, pair_number_count, not_pair_number_count))
