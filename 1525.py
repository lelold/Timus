n, m, k = map(int, input().split())
ins = input()
minn, minm, mink = 0, 0, 0
maxn, maxm, maxk = 0, 0, 0
curn, curm, curk = 0, 0, 0
for i in ins:
    if i == 'l':
        curn -= 1
    elif i == 'r':
        curn += 1
    elif i == 'd':
        curm -= 1
    elif i == 'u':
        curm += 1
    elif i == 'b':
        curk -= 1
    elif i == 'f':
        curk += 1
    maxn, minn = max(maxn, curn), min(minn, curn)
    maxm, minm = max(maxm, curm), min(minm, curm)
    maxk, mink = max(maxk, curk), min(mink, curk)
resn = n - (maxn - minn) if n - (maxn - minn) >= 1 else 1
resm = m - (maxm - minm) if m - (maxm - minm) >= 1 else 1
resk = k - (maxk - mink) if k - (maxk - mink) >= 1 else 1
print(resn * resm * resk)
