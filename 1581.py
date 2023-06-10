from array import array


n = int(input())
nums = array('i', map(int, input().split()))
sum_nums = nums[0]
c = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        sum_nums += nums[i]
        c += 1
    else:
        print(c, sum_nums // c, end=' ')
        sum_nums = nums[i]
        c = 1
print(c, sum_nums // c)
