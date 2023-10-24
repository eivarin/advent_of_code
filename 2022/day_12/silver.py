day, year, part = (12, 2022, "a")

from dijkstar import Graph, find_path

def bla(coords, starting_matrix, G: Graph, m): 
    x, y = coords
    poss_adj = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    poss_adj = list(filter(lambda c: c[0]<len(starting_matrix[0]) and c[0]>-1 and c[1]>-1 and c[1]<len(starting_matrix), poss_adj))
    char = starting_matrix[y][x]
    if char == "S":
        char = "a"
    if char != "E":
        height = ord(char)
        for px,py in poss_adj:
            new_char = starting_matrix[py][px]
            if new_char == "S":
                new_char = "a"
            elif new_char == "E":
                new_char = "z"
            if ord(new_char) <= height+1:
                G.add_edge(m[coords],m[(px,py)])
    return G


def solve(input):
    lns = input.splitlines()
    x=0
    y=0
    start=(x,y)
    end=(x,y)
    points = {}
    i=0
    for l in lns:
        x=0
        for c in l:
            if c in ["S"]:
                start = (x,y)
            elif c == "E":
                end=(x,y)
            points[(x,y)] = i
            x+=1
            i+=1
        y+=1
    x=0
    y=0
    G = Graph()
    for l in lns:
        x=0
        for c in l:
            G = bla((x,y), lns, G, points)
            x+=1
        y+=1
    plist = find_path(G, points[start], points[end], cost_func= lambda x,y,z,w : 1)

    return plist.total_cost

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()