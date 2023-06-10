n = int(input())
c = n + 2
for i in range(n):
    guest = input()
    if guest[-4:] == '+one':
        c += 1
print(1400 if c == 13 else c * 100)
