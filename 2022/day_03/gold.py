day, year, part = (3, 2022, "b")

def solve(input):
    lns = input.split("\n")
    result = 0
    i=2
    while i < len(lns):
        elf1 = set(lns[i])
        elf2 = set(lns[i-1])
        elf3 = set(lns[i-2])
        item = list(elf1.intersection(elf2.intersection(elf3)))[0]
        prio = (ord(item) - 96) if item.islower() else (ord(item) - 38)
        result +=prio
        i+=3
    return result

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()