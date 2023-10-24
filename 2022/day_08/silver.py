day, year, part = (8, 2022, "a")
import numpy as np
def solve(input):
    lns = [list(map(lambda y: int(y), x)) for x in input.splitlines()]
    cols = np.array(lns).T.tolist()
    visible_trees = set()
    y=0
    for l in lns:
        x=0
        for i in l:
            before =  l[:x]
            after = l[x+1:]
            if not (len(before) and max(before) >= i):
                visible_trees.add((x,y))
            if not (len(after) and max(after) >= i):
                visible_trees.add((x,y))
            x+=1
        y+=1
    y=0
    x=0
    for l in cols:
        y=0
        for i in l:
            before =  l[:y]
            after = l[y+1:]
            if not (len(before) and max(before) >= i):
                visible_trees.add((x,y))
            if not (len(after) and max(after) >= i):
                visible_trees.add((x,y))
            y+=1
        x+=1
    return len(visible_trees)

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()