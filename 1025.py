def sort_vst(lst):
    """
    Takes an iterable and sorts using insertion algorithm.
    """
    for i in range(1, len(lst)):
        temp = lst[i]
        pos = i - 1
        while pos >= 0 and temp < lst[pos]:
            lst[pos + 1] = lst[pos]
            pos -= 1
        lst[pos + 1] = temp


n = int(input())
izbirateli = list(map(int, input().split()))
res = 0
sort_vst(izbirateli)
bolshinstvo = n // 2 if n % 2 == 0 else n // 2 + 1
for j in range(bolshinstvo):
    res += izbirateli[j] // 2 if izbirateli[j] % 2 == 0 else izbirateli[j] // 2 + 1
print(res)
