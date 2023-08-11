day, year, part = (6, 2022, "b")

def solve(input):
    l = input.split("\n")[0]
    i=0
    n=14
    while i+3<len(l):
        start = set()
        for x in range(n):
            start.add(l[i+x])
        if len(list(start)) == n:
            break
        i+=1
    return i+n

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()