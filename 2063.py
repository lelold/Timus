from random import randint


m = int(input())
j = 1
for i in range(m):
    j += 1
    for k1 in range(1, j + 1):
        for k2 in range(1, j):
            print(f'? {k2} {k2 + 1}')
    guess = randint(1, j-1)
    print(f'! {guess} {guess + 1}')
