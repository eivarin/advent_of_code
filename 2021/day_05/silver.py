f = open("input.txt")
lns = f.read().splitlines()

ts = []
# transform in tuples
for l in lns:
    st1, st2 = l.split(" -> ")
    t1 = st1.split(",")
    t2 = st2.split(",")
    ts.append((t1,t2))
print(ts)
points = []
# transform in points
