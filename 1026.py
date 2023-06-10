def counting_sort(arr):
    """
    Takes an iterable and sorts using counting algorithm.
    """
    aux_len = max(arr) + 1
    aux = [0] * aux_len
    for i in arr:
        aux[i] += 1
    for i in range(1, aux_len):
        aux[i] += aux[i-1]
    res = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        num_i = arr[i]
        aux[num_i] -= 1
        m = aux[num_i]
        res[m] = num_i
        i -= 1
    return res


n = int(input())
db = n * [0]
for ind in range(n):
    db[ind] = int(input())
input()
k = int(input())
db = counting_sort(db)
for ind in range(k):
    print(db[int(input()) - 1])
