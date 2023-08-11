import aocd
day, year, part = (5, 2022, "b")


def solve(input):
    lns = input.split("\n")
    stacks = []

    inst_start = 0

    for l in lns:
        cs = 0
        i = 0
        if l[1].isdigit():
            inst_start += 2
            break
        while i < len(l):
            if cs >= len(stacks):
                stacks.append([])
            if l[i] == "[":
                stacks[cs].append(l[i+1])
            i += 4
            cs += 1
        inst_start += 1

    for s in stacks:
        s.reverse()
    for l in lns[inst_start:]:
        if l[0] == "":
            continue
        _, n, _, s, _, d = l.split()
        n = int(n)
        s = int(s) - 1
        d = int(d) - 1
        lifted = []
        while n:
            crate = stacks[s].pop()
            lifted.append(crate)
            n -= 1
        lifted.reverse()
        for crate in lifted:
            stacks[d].append(crate)
    result = ""
    for s in stacks:
        result += s[-1]
    return result


def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(
        f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)


if __name__ == "__main__":
    main()
