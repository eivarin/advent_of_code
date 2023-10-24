day, year, part = (13, 2022, "a")
from ast import literal_eval


def solve(input):
    lns = input.split("\n\n")
    pairs = []
    for l in lns:
        pairs.append([literal_eval(s) for s in l.split("\n")])


    def compare_pair(p):
        left, right = p
        if type(left) == type(right):
            if type(left) == type([]):
                i = 0
                while i < len(left) and i < len(right):
                    r = compare_pair((left[i],right[i]))
                    if r != None:
                        return r
                    i+=1
                if len(left) == len(right):
                    return None
                elif len(left) < len(right):
                    return True
                else:
                    return False
            elif type(left) == type(0):
                if left == right:
                    return None
                elif left < right:
                    return True
                else:
                    return False
        else:
            if type(left) == type(0):
                return compare_pair(([left],right))
            else:
                return compare_pair((left,[right]))

    result = list(map(compare_pair, pairs))
    i=1
    res=0
    for r in result:
        if r:
            res+=i
        i+=1
    return res

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()