from math import ceil

n, k = map(int, input().split())
all_beef_minutes = n * 2
beef_minutes_velocity = k
if k > n:
    print(2)
else:
    print(ceil(all_beef_minutes / beef_minutes_velocity))
