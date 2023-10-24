day, year, part = (8, 2022, "b")
import numpy as np
def solve(input):
    lns = [list(map(lambda y: int(y), x)) for x in input.splitlines()]
    cols = np.array(lns).T.tolist()
    visible_trees = {}


    y=0
    for l in lns:
        x=0
        for i in l:
            visible_trees[(x,y)] = [0, 0, 0, 0]
            before =  l[:x]
            before.reverse()
            after = l[x+1:]
            for i1 in before:
                visible_trees[(x,y)][0]+=1
                if i1 >= i:
                    break
            for i1 in after:
                visible_trees[(x,y)][1]+=1
                if i1 >= i:
                    break
            x+=1
        y+=1
    y=0
    x=0
    for l in cols:
        y=0
        for i in l:
            before =  l[:y]
            before.reverse()
            after = l[y+1:]
            for i1 in before:
                visible_trees[(x,y)][2]+=1
                if i1 >= i:
                    break
            for i1 in after:
                visible_trees[(x,y)][3]+=1
                if i1 >= i:
                    break
            y+=1
        x+=1
    results = []
    for tree in visible_trees:
        a,b,c,d = visible_trees[tree]
        results.append(a*b*c*d)
    results.sort()
    return results[-1]

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()