day, year, part = (4, 2022, "b")

def solve(input):
    lns = input.split("\n")
    total = 0
    for l in lns:
        sections = set()
        l1,l2 = [l.split("-") for l in l.split(",")]
        elf1 = list(range(int(l1[0]),int(l1[1]) + 1))
        has_overlaped = False
        for point in elf1:
            if point not in sections:
                sections.add(point)
            elif not has_overlaped:
                has_overlaped = True
        elf2 = list(range(int(l2[0]),int(l2[1]) + 1))
        has_overlaped = False
        for point in elf2:
            if point not in sections:
                sections.add(point)
            elif not has_overlaped:
                has_overlaped = True
        if has_overlaped:
            total+=1
    return total

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()