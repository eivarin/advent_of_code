from aocd import get_data
lns = get_data(day=10, year=2021).splitlines()
# f = open("input.txt")
# lns = f.read().splitlines()

ichars = {")": 0, "]": 0, "}": 0, ">": 0}

for l in lns:
    cs = []
    for c in l:
        match c:
            case "<":
                cs.append(">")
            case "(":
                cs.append(")")
            case "[":
                cs.append("]")
            case "{":
                cs.append("}")
            case _:
                if c == cs[-1]:
                    cs.pop()
                else:
                    ichars[c] += 1
                    break

print(ichars[")"]*3 + ichars["]"]*57 + ichars["}"]*1197 + ichars[">"]*25137)