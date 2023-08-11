day, year, part = (3, 2022, "a")

def solve(input):
    lns = input.split("\n")
    result = 0
    for l in lns:
        sack1 = set(l[:int(len(l)/2)])
        sack2 = set(l[int(len(l)/2):])
        item = list(sack1.intersection(sack2))[0]
        prio = (ord(item) - 96) if item.islower() else (ord(item) - 38)
        result +=prio
    return result

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()