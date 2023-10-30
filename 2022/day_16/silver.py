day, year, part = (16, 2022, "a")
import re
valves = {}
open_valves = set()
curr = "AA"
total_pressure_released = 0
minutes = 30

def calc_potential_pressure(x, used_nodes=set()):
    global valves
    used_nodes.add(x)
    l = [n for n in valves[x][1]]
    rl = [calc_potential_pressure(n, set(list(used_nodes))) for n in l if not n in used_nodes]
    result = None
    for r in rl:
        print(f"r: {r}")
    if len(rl) > 0:
        result = max(rl, key=lambda x: x[1])
        repeated = [x for x in rl if x[1] == result[1]]
        if len(repeated) > 1:
            result = min(repeated, key=lambda x: len(x[0]))
    else:
        result = ([], 0)

    return ([(x,valves[x][0])]+result[0], (result[1]) + valves[x][0] * (30-len(result[0])))

def solve(input):
    global valves, open_valves, curr, total_pressure_released
    curr_releasing_pressure = 0
    for l in input.splitlines():
        srch = re.search(r'Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ((\w\w(, )?)+)',l)
        name, flow, cons = [t(s) for t,s in zip((lambda x: x,int,lambda x: x.split(", ")),srch.groups())]
        valves[name] = (flow,cons)
    i = 1
    while i <= minutes:
        curr_flow, adjacents = valves[curr]
        if curr_flow > 0 and not curr in open_valves:
            print(f"Valves open: {open_valves}, Pressure per minute: {curr_releasing_pressure}\nOpening: {curr}\n")
            open_valves.add(curr)
            curr_releasing_pressure += curr_flow
            valves[curr] = (0,valves[curr][1])
        else:
            test = calc_potential_pressure(curr, set())
            print(f"Valves open: {open_valves}, Pressure per minute: {curr_releasing_pressure}\nMoving to: {test}\n")
            curr = test[0][1][0]
        total_pressure_released += curr_releasing_pressure
        i += 1
    return total_pressure_released

import aocd
def main():
    # data = aocd.get_data(day=day, year=year)
    data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    # aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()