from sys import stdin, stdout


s = [[] for i in range(123)]
f = int(stdin.readline())
in_arr = stdin.readline().strip()
x = f - 1
for i in range(len(in_arr)):
    s[ord(in_arr[i])].append(i)
n = [j for i in range(123) for j in s[i]]
length = len(n)
for i in range(length):
    x = n[x]
    stdout.write(in_arr[x])
