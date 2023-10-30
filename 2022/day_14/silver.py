day, year, part = (14, 2022, "a")

m = set()
last_height = 0

def update_last_height(y):
    global last_height
    if y > last_height:
        last_height = y

def fall_sand():
    global m, last_height
    pos = (500,0)
    while pos[1] < last_height:
        if not (pos[0], pos[1]+1) in m:
            pos = (pos[0], pos[1]+1)
        elif not (pos[0]-1, pos[1]+1) in m:
            pos = (pos[0]-1, pos[1]+1)
        elif not (pos[0]+1, pos[1]+1) in m:
            pos = (pos[0]+1, pos[1]+1)
        else:
            break
    else:
        # print(pos)
        return True
    # print(pos)
    m.add(pos)
    return False

def solve(input):
    global m, last_height
    paths = [l.split(" -> ") for l in input.split("\n")]
    for rocks in paths:
        rocks = list(map(lambda x: (int(x[0]), int(x[1])), [r.split(",") for r in rocks]))
        start_rock = rocks[0]
        update_last_height(start_rock[1])
        for end_rock in rocks[1:]:
            update_last_height(end_rock[1])
            rock_range = set()
            if start_rock[0] == end_rock[0]:
                bigger, smaller = (start_rock[1], end_rock[1]) if start_rock[1] > end_rock[1] else (end_rock[1], start_rock[1])
                rock_range = set([(start_rock[0], ry) for ry in range(smaller, bigger+1)])
            else:
                bigger, smaller = (start_rock[0], end_rock[0]) if start_rock[0] > end_rock[0] else (end_rock[0], start_rock[0])
                rock_range = set([(rx, start_rock[1]) for rx in range(smaller, bigger+1)])
            m = m.union(rock_range)
            start_rock = end_rock
    i=0
    while True:
        if fall_sand():
            break
        else:
            i+=1
    return i



import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()