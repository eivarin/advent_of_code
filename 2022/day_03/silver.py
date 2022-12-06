f = open("input.txt")
lns = f.read().splitlines()
result = 0
for l in lns:
    sack1 = set(l[:int(len(l)/2)])
    sack2 = set(l[int(len(l)/2):])
    item = list(sack1.intersection(sack2))[0]
    prio = (ord(item) - 96) if item.islower() else (ord(item) - 38)
    result +=prio
print(result)