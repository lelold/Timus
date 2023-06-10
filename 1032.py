n, inps, nums = int(input()), [], [-1 for i in range(10000)]
nums[0], ind = 0, 0
for i in range(n):
    inps.append(int(input()))
summa = inps[0]
mod = summa % n
while nums[mod] == -1:
    nums[mod] = ind + 1
    ind += 1
    summa += inps[ind]
    mod = summa % n
else:
    print(ind - nums[mod] + 1)
    for j in range(nums[mod], ind + 1):
        print(inps[j])