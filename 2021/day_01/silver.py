f = open("input.txt")
lns= f.readlines()

result = 0
prev = int(lns[0])
for l in lns[1:]:
    result+= 1 if int(l) > prev else 0
    prev = int(l)

print(result)