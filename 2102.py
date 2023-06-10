from math import sqrt


n = int(input())
sumn, current, res = 0, n, 'Yes'
for i in range(2, int(sqrt(n)) + 1):
    if i > current:
        break
    while current % i == 0:
        sumn += 1
        current //= i
    if sumn > 20:
        res = 'No'
        break
    elif sumn == 20:
        if current != 1:
            res = 'No'
        break
    elif sumn == 19:
        if (i + 1) ** 2 > current:
            if i + 1 <= current:
                break
            else:
                res = 'No'
                break
    if (i + 1) ** (20 - sumn) > current:
        res = 'No'
        break
if res and current != 1:
    sumn += 1
if sumn != 20:
    res = 'No'
print(res)
