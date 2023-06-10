n = int(input())
q = ''
if n == 0:
    print(10)
    exit()
elif n == 1:
    print(1)
    exit()
else:
    for i in range(9, 1, -1):
        while n % i == 0:
            n /= i
            q += str(i)
if n == 1:
    print(q[::-1])
else:
    print(-1)
