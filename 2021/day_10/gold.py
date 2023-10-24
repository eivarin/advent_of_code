from aocd import get_data
lns = get_data(day=10, year=2021).splitlines()
# f = open("input.txt")
# lns = f.read().splitlines()

print(lns)

ichars = {")": 0, "]": 0, "}": 0, ">": 0}
iline = []
i=0
while i<len(lns):
    l = lns[i]
    cs = []
    incomplete = True
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
                    incomplete = False
                    break
    if incomplete:
        iline.append(cs)
    print(iline)
    i+=1

def part2_aux(s):
    r = 0
    s.reverse()
    for c in s:
        r*=5
        match c:
            case ')':
                r+=1
            case ']':
                r+=2
            case '}':
                r+=3
            case '>':
                r+=4
    return r

result = list(map(part2_aux, iline))
result.sort()
print(result)
print(result[int(len(result)/2)])