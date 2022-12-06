f = open("input.txt")
lns= f.read().splitlines()




oxigen_pvalues = set()
scrubber_pvalues = set()
for l in lns:
    oxigen_pvalues.add(l)
    scrubber_pvalues.add(l)

def aux(lns, pos):
    checks = [0,0]
    for l in lns:
        b = l[pos]
        checks[0 if b == "0" else 1] += 1
    return checks

print(oxigen_pvalues)
print(scrubber_pvalues)



for pos in range(len(lns[0])):
    b = 0
    zeros, ones = aux(oxigen_pvalues, pos)
    b = 0 if zeros <= ones else 1
    if len(oxigen_pvalues) > 1:
        oxigen_pvalues = set(filter(lambda x: (int(x[pos])  == b), oxigen_pvalues))
    else:
        break
    
for pos in range(len(lns[0])):
    b = 0
    zeros, ones = aux(scrubber_pvalues, pos)
    b = 1 if zeros <= ones else 0
    if len(scrubber_pvalues) > 1:
        scrubber_pvalues = set(filter(lambda x: (int(x[pos])  == b), scrubber_pvalues))
    else:
        break



a = list(oxigen_pvalues)
b = list(scrubber_pvalues)
print(a)
print(b)
gamma = int(a[0], 2)
epsilon = int(b[0], 2)

result = gamma * epsilon
print(result)