def qsort(lst):
    """
    Takes an iterable and sorts using quick sort algorithm.
    """
    if len(lst) < 2:
        return lst
    opor = lst[0]
    less = [i for i in lst[1:] if i <= opor]
    greater = [i for i in lst[1:] if i > opor]
    return qsort(less) + [opor] + qsort(greater)


n = int(input())
summoists = []
rounds = 2 ** n
for j in range(rounds):
    summoists.append(input())
prefectures = [i.split()[-1] for i in summoists]
prefectures_dict = {}
for j in prefectures:
    if j not in prefectures_dict.keys():
        prefectures_dict[j] = 1
    else:
        prefectures_dict[j] += 1
prefectures_max_count = max(prefectures_dict.values())
c = 0
while prefectures_max_count <= rounds // 2:
    rounds = rounds // 2
    c += 1
print(c)
