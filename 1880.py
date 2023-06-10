def shaker_sort(lst):
    """
    Takes an iterable and sorts using shaker sort algorithm.
    """
    left = 0
    right = len(lst) - 1
    while left <= right:
        for i in range(left, right, 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        right -= 1
        for i in range(right, left, -1):
            if lst[i - 1] > lst[i]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        left += 1
    return lst


sets = []
for ind in range(3):
    n = int(input())
    integers = set(map(int, input().split()))
    sets.append(integers)
shaker_sort(sets)
common_integers = set.intersection(*sets)
print(len(common_integers))
