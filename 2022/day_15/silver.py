day, year, part = (15, 2022, "a")

import re
manhatan_dist = lambda p1,p2: sum(abs(val1-val2) for val1, val2 in zip(p1,p2))

drones = [[],[],[]]


magicrow = 2000000

def solve(input):
    minx, maxx = (0,4000000)
    occupied_row = set()
    beacons_row = set()
    for l in input.splitlines():
        x,y,cx,cy = [t(s) for t,s in zip((int,int,int,int),re.search('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)',l).groups())]
        new_drone = ((x,y),manhatan_dist((x,y),(cx,cy)))
        if cy == magicrow:
            beacons_row.add(cx)
        if y<magicrow:
            drones[0].append(new_drone)
        elif y==magicrow:
            drones[1].append(new_drone)
        else:
            drones[2].append(new_drone)
    for d in drones[1]:
        coords = d[0]
        occupied_row.add(coords[0])
        for x in range(coords[0]+1,coords[0]+d[1]+1):
            occupied_row.add(x)
        for x in range(coords[0]-d[1], coords[0]):
            occupied_row.add(x)
    for d in drones[0]:
        coords = d[0]
        dist_to_row=coords[1]+d[1]-magicrow
        if dist_to_row > 0:
            occupied_row.add(coords[0])
            for x in range(coords[0]+1,coords[0]+dist_to_row+1):
                occupied_row.add(x)
            for x in range(coords[0]-dist_to_row, coords[0]):
                occupied_row.add(x)
    for d in drones[2]:
        coords = d[0]
        dist_to_row=magicrow-(coords[1]-d[1])
        if dist_to_row > 0:
            occupied_row.add(coords[0])
            for x in range(coords[0]+1,coords[0]+dist_to_row+1):
                occupied_row.add(x)
            for x in range(coords[0]-dist_to_row, coords[0]):
                occupied_row.add(x)
    return len(occupied_row - beacons_row)

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
#     data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()