day, year, part = (4, 2022, "a")

def solve(input):
    lns = input.split("\n")
    total = 0
    for l in lns:
        l1,l2 = [l.split("-") for l in l.split(",")]
        elf1 = set(range(int(l1[0]),int(l1[1]) + 1))
        elf2 = set(range(int(l2[0]),int(l2[1]) + 1))
        common = elf1.intersection(elf2)
        if common == elf1 or common == elf2:
            total +=1
    return total

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()