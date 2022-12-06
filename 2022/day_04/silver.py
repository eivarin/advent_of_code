f = open("input.txt")
lns = f.read().splitlines()

total = 0
for l in lns:
    l1,l2 = [l.split("-") for l in l.split(",")]
    elf1 = set(range(int(l1[0]),int(l1[1]) + 1))
    elf2 = set(range(int(l2[0]),int(l2[1]) + 1))
    common = elf1.intersection(elf2)
    if common == elf1 or common == elf2:
        total +=1
print(total)