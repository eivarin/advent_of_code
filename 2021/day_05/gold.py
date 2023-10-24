f = open("input.txt")
lns = f.read().splitlines()

ts = []
# transform in tuples
for l in lns:
    st1, st2 = l.split(" -> ")
    t1 = [int(coor) for coor in st1.split(",")]
    t2 = [int(coor) for coor in st2.split(",")]
    ts.append((t1,t2))
points = {}

def get_diagonal_points(start_x, start_y, end_x, end_y):
    # make start_x <= end_x, if you don't need to check, remove this line
    if start_x > end_x:
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y

    result = []
    slope = (end_y - start_y) // (end_x - start_x)
    for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
        result.append((i,j))
    result.append((end_x,end_y))  # add end point
    return result

for (xs, ys), (xe,ye) in ts:
    if xs == xe:
        x = xs
        ys,ye = (min(ys,ye), max(ys,ye))
        for y in range(ys,ye+1):
            points[(x,y)] = (points[(x,y)] + 1) if (x,y) in points else 1
    elif ys == ye:
        y = ys
        xs,xe = (min(xs,xe), max(xs,xe))
        for x in range(xs,xe+1):
            points[(x,y)] = (points[(x,y)] + 1) if (x,y) in points else 1
    elif abs(xs-xe) == abs(ys-ye):
        for p in get_diagonal_points(xs,ys,xe,ye):
            points[p] = (points[p] + 1) if p in points else 1
result = 0
for p in points:
    result += 1 if points[p]>1 else 0
print(result)
# transform in points
