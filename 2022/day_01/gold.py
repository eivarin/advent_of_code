day, year, part = (1, 2022, "b")

def solve(input):
    lns = input.split("\n")
    elves = [[]]
    i = 0
    new_elf_next = False
    for l in lns:
        if l == "" or l == "\n":
            new_elf_next = True
        else:
            if new_elf_next:
                new_elf_next = False
                i+=1
                elves.append([])
            elves[i].append(int(l))

    result = [sum(elf) for elf in elves]
    result.sort()
    return result[-1] + result[-2] + result[-3]

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()