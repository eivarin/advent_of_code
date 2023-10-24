day, year, part = (10, 2022, "b")

def solve(input):
    lns = [l.split() for l in input.splitlines()]
    X=1
    cycle=1

    crt=[""]
    crt_line = 0

    def draw_in_CRT(cycle, X, crt, crt_line):
        if (cycle-1) // 40 != crt_line:
            crt.append("")
            crt_line+=1
        crt[crt_line] += "#" if (cycle-1) % 40 in [X-1,X,X+1] else "."
        return crt, crt_line

    for l in lns:
        if len(l) == 1:
            crt, crt_line = draw_in_CRT(cycle, X, crt, crt_line)
            cycle+=1
        else:
            crt, crt_line = draw_in_CRT(cycle, X, crt, crt_line)
            cycle+=1
            crt, crt_line = draw_in_CRT(cycle, X, crt, crt_line)
            cycle+=1
            X += int(l[1])
            
    for s in crt:
        print(s)
    return 0

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print("submit the ansewr manually")
    # print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    # aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()