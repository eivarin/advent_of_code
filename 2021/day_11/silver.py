from aocd import get_data
lns = get_data(day=11, year=2021).splitlines()
# f = open("input.txt")
# lns = f.read().splitlines()

m = {}

x=0
y=0
for l in lns:
    for c in l:
        m[(x,y)] = int(c)
        x+=1
    x=0
    y+=1

def p1(m):
    for p in m:
        m[p]+=1
    return m

def p2(m):
    l_flashed = set()
    flashed = True
    while flashed:
        flashed = False
        for p in m:
            if m[p] > 9 and p not in l_flashed:
                l_flashed.add(p)
                flashed = True
                for y in [p[1]-1, p[1], p[1]+1]:
                    for x in [p[0]-1, p[0], p[0]+1]:
                        if (x,y) in m:
                            m[(x,y)] += 1 if (x,y) != p  else 0
    return m, l_flashed

def p3(m, l_flashed):
    for p in l_flashed:
        m[p] = 0
    return m


r = 0
i=0
while i<100:
    m = p1(m)
    m, lf = p2(m)
    r += len(lf)
    m = p3(m,lf)
    i+=1

print(r)