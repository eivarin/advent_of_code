day, year, part = (10, 2022, "a")

def solve(input):
    lns = [l.split() for l in input.splitlines()]
    imp_cycles = {20,60,100,140,180,220}
    X=1
    cycle=1

    result = 0

    def check_cycle(lst, cycle, X, result):
        if cycle in lst:
            result+= X*cycle
        return result
        
    for l in lns:
        if len(l) == 1:
            result = check_cycle(imp_cycles,cycle,X,result)
            cycle+=1
        else:
            result = check_cycle(imp_cycles,cycle,X,result)
            cycle+=1
            result = check_cycle(imp_cycles,cycle,X,result)
            cycle+=1
            X += int(l[1])
    return result

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()