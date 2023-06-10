inp = input()
harry_cans, larry_cans = int(inp.split()[0]), int(inp.split()[1])
cans = harry_cans + larry_cans - 1
print("%s %s" % (cans - harry_cans, cans - larry_cans), end='')
