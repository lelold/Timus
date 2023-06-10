n = int(input())
m = []
sumn = 0
c5 = 0
for i in range(n):
    m.append(int(input()))
    sumn += m[i]
    if m[i] == 3:
        print('None')
        exit()
    if m[i] == 5:
        c5 += 1
if c5 == n:
    print('Named')
elif c5 != n and sumn / n >= 4.5:
    print('High')
else:
    print('Common')
