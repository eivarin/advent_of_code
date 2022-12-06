f = open("input.txt")
lns = f.read().splitlines()
result = 0
i=2
while i < len(lns):
    elf1 = set(lns[i])
    elf2 = set(lns[i-1])
    elf3 = set(lns[i-2])
    item = list(elf1.intersection(elf2.intersection(elf3)))[0]
    prio = (ord(item) - 96) if item.islower() else (ord(item) - 38)
    result +=prio
    i+=3
print(result)