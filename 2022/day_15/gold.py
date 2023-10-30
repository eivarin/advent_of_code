day, year, part = (15, 2022, "b")

import re
manhatan_dist = lambda p1,p2: sum(abs(val1-val2) for val1, val2 in zip(p1,p2))

drones = []

def solve(input):
    minc, maxc= (0,4000000)
    possible_coords = set()
    for l in input.splitlines():
        x,y,cx,cy = [t(s) for t,s in zip((int,int,int,int),re.search('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)',l).groups())]
        new_drone = ((x,y),manhatan_dist((x,y),(cx,cy)))
        drones.append(new_drone)
    rx,ry = (0,0)
    possible_coords = set()
    for di, (coords, dist) in enumerate(drones):
        print(f"Drone {di}")
        maxy=coords[1]+dist
        possible_coords = {(coords[0],coords[1]-dist-1), (coords[0],maxy+1)}
        for yi,y in enumerate(range(coords[1]-dist, maxy+1)):
            minx, maxx = (coords[0]-yi-1, coords[0]+yi+1)
            possible_coords.add((minx,y))
            possible_coords.add((maxx,y))
        for c in possible_coords:
            no_colision = True
            for d in drones:
                di = manhatan_dist(c,d[0])
                if di<=d[1]:
                    # print(f"Colision at {c} with {d}")
                    no_colision = False
                    break
            if no_colision and c[0] > minc and c[0] < maxc and c[1] < maxc and c[1] > minc:
                rx,ry = c
                return rx*maxc+ry
    return 0

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()