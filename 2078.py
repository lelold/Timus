a = [int(i) for i in input().split()]
mins = sum(a) + 10 if a[8] == 10 and a[9] > 20 else sum(a)
maxs = a[0] + a[1] if a[0] != 10 else a[0] + 2 * a[1]
for i in range(2, 10):
    if i != 9:
        if a[i-1] == 10 and a[i-1] != a[i-2]:
            maxs += 2 * a[i]
        elif a[i-1] == a[i-2] == 10:
            maxs += 3 * a[i]
        else:
            maxs += a[i]
    else:
        if a[i - 1] == 10 and a[i - 1] != a[i - 2]:
            if a[i] <= 20:
                maxs += a[i] * 2
            else:
                maxs += 40 + a[i] - 20
        elif a[i - 1] == a[i - 2] == 10:
            if a[i] <= 10:
                maxs += a[i] * 3
            elif 10 < a[i] <= 20:
                maxs += 30 + (a[i] - 10) * 2
            else:
                maxs += 50 + a[i] - 20
        else:
            maxs += a[i]
print(mins, maxs)
