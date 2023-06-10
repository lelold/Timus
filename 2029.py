n = int(input())
inp, res, empty_pin = input(), 0, 0
for i in range(n - 1, -1, -1):
    s = ord(inp[i]) - ord('A')
    if empty_pin != s:
        res += 2 ** i
        empty_pin = 3 - empty_pin - s
print(res)
