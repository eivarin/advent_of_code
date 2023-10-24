day, year, part = (13, 2022, "b")
import functools
from ast import literal_eval


def solve(input):
    pairs = []
    lns = input.split("\n\n")
    for l in lns:
        pairs.extend([literal_eval(s) for s in l.split("\n")])


    def compare_pair(left, right):
    # def compare_pair(pair):
    #     left, right = pair
        if type(left) == type(right):
            if type(left) == type([]):
                i = 0
                while i < len(left) and i < len(right):
                    r = compare_pair(left[i],right[i])
                    if r != 0:
                        return r
                    i+=1
                if len(left) == len(right):
                    return 0
                elif len(left) < len(right):
                    return -1
                else:
                    return 1
            elif type(left) == type(0):
                if left == right:
                    return 0
                elif left < right:
                    return -1
                else:
                    return 1
        else:
            if type(left) == type(0):
                return compare_pair([left],right)
            else:
                return compare_pair(left,[right])

    pairs.extend([[[2]], [[6]]])
    pairs = sorted(pairs, key=functools.cmp_to_key(compare_pair))

    r = 1
    i=1
    for e in pairs:
        # print(e)
        if e in [[[2]],[[6]]]:
            r*=i
        i+=1
    return r

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()