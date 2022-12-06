f = open("input.txt")
lns= f.read().splitlines()

checks = [[0,0] for n in range(len(lns[0]))]


for l in lns:
    i = 0
    for b in l:
        checks[i][0 if b == "1" else 1] += 1
        i+=1

checks.reverse()

gamma = 0
epsilon = 0
i = 1
for c in checks:
    if c[0] > c[1]:
        gamma +=i
    else:
        epsilon +=i
    i*=2


result = gamma * epsilon
print(result)