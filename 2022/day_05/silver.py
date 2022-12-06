f = open("input.txt")
lns = f.read().splitlines()
stacks = []

inst_start = 0

for l in lns:
    cs = 0
    i=0
    if l[1].isdigit():
        inst_start += 2
        break
    while i<len(l):
        if cs>=len(stacks):
            stacks.append([])
        if l[i] == "[":
            stacks[cs].append(l[i+1])
        i+=4
        cs+=1
    inst_start+=1
    
print(stacks)
for s in stacks:
    s.reverse()

for l in lns[inst_start:]:
    if l[0] == "":
        print("aaaaaaaaaaaa")
        continue
    _, n, _, s, _, d = l.split()
    n = int(n)
    s = int(s) - 1
    d = int(d) - 1
    while n:
        print(s)
        crate = stacks[s].pop()
        stacks[d].append(crate)
        n-=1

result = ""
for s in stacks:
    result+=s[-1]
    print(s)

print(result)