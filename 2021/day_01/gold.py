f = open("input.txt")
lns= [int(l) for l in f.readlines()]

windows = []
i=0
for l in lns:
    windows.append(l)
    if i>0:
        windows[i-1] += l
    if i>1:
        windows[i-2] += l
    i+=1

result = 0
prev = windows[0]
for l in windows[1:]:
    result+= 1 if l > prev else 0
    prev = l

print(result)