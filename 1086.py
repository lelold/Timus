from math import log


def sieve(num):
    if num < 2:
        return []
    primes_nums = [1] * num
    for i in range(2, int(num ** 0.5) + 1):
        if primes_nums[i - 2]:
            for j in range(i + i, num + 1, i):
                primes_nums[j - 2] = 0
    return primes_nums


n = int(input())
nums = []
for j in range(n):
    nums.append(int(input()))
primes = sieve(int(1.5 * max(nums) * log(max(nums))) + 1)
n_primes = []
for j in range(len(primes) - 1):
    n_primes.append(j + 2) if primes[j] == 1 else True
for j in nums:
    print(n_primes[j-1])
