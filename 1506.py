from math import ceil

n, k = map(int, input().split())
a = [i for i in map(int, input().split())]
matrix_height = ceil(n / k)
for i in range(matrix_height):
    for j in range(k):
        try:
            print('{:>4}'.format(a[i + j * matrix_height]), end='')
        except IndexError:
            print('    ', end='')
    if i == matrix_height - 1:
        break
    print('')
