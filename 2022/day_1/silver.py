f = open("input.txt", "r")

lns = f.readlines()

elves = [[]]
i = 0
new_elf_next = False
for l in lns:
    if l == "" or l == "\n":
        new_elf_next = True
    else:
        if new_elf_next:
            new_elf_next = False
            i+=1
            elves.append([])
        elves[i].append(int(l))

result = [sum(elf) for elf in elves]
result.sort()
print(result[-1])