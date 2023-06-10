n = int(input())
balls = [int(input()) for i in range(n)]
flag = True
expected_ind1, expected_ind2, expected_ind3 = 0, 0, 0
expected = [0 for j in range(n)]
while expected_ind1 < n:
    if expected_ind3 > 0 and expected[expected_ind3 - 1] == balls[expected_ind1]:
        expected_ind3 -= 1
        expected_ind1 += 1
    elif expected_ind2 < n:
        expected_ind2 += 1
        expected[expected_ind3] = expected_ind2
        expected_ind3 += 1
    else:
        flag = False
        break
print('Not a proof' if flag else 'Cheater')
