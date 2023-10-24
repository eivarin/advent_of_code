day, year, part = (9, 2022, "a")

def solve(input):
    lns = [l.split() for l in input.splitlines()]
    head = [0,0]
    tail = [0,0]

    def dist(p,q):
        return max([abs(p[0] - q[0]),abs(p[1] - q[1])])

    def move_head(h, m):
        match m:
            case "U":
                h[1]+=1
            case "D":
                h[1]-=1
            case "R":
                h[0]+=1
            case "L":
                h[0]-=1
        return h

    def try_move_tail(h,t):
        if dist(h,t)>1:
            if h[0] == t[0]+2:
                t = [h[0]-1,h[1]]
            elif h[0] == t[0]-2:
                t = [h[0]+1,h[1]]
            elif h[1] == t[1]+2:
                t = [h[0],h[1]-1]
            elif h[1] == t[1]-2:
                t = [h[0],h[1]+1]
        return t


    t_poss = set()
    t_poss.add((tail[0],tail[1]))
    for move, times in lns:
        times = int(times)
        while times:
            times-=1
            head = move_head(head,move)
            tail = try_move_tail(head,tail)
            t_poss.add((tail[0],tail[1]))
    return len(t_poss)

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()