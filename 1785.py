num = int(input())

if 1 <= num <= 4:
    print('few')
elif 5 <= num <= 9:
    print('several')
elif 10 <= num <= 19:
    print('pack')
elif 20 <= num <= 49:
    print('lots')
elif 50 <= num <= 99:
    print('horde')
elif 100 <= num <= 249:
    print('throng')
elif 250 <= num <= 499:
    print('swarm')
elif 500 <= num <= 999:
    print('zounds')
elif 1000 <= num:
    print('legion')
