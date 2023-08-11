day, year, part = (2, 2022, "a")

def solve(input):
    lns = input.split("\n")
    total=0
    for l in lns:
        plays = l.split()
        p1, p2 = plays
        shape_score = 0
        match p2:
            case "X":
                shape_score = 1
            case "Y":
                shape_score = 2
            case "Z":
                shape_score = 3
        match_score = 0
        match p1:
            case "A":
                if shape_score == 1:
                    match_score = 3
                elif shape_score == 2:
                    match_score = 6
                else:
                    match_score = 0
            case "B":
                if shape_score == 1:
                    match_score = 0
                elif shape_score == 2:
                    match_score = 3
                else:
                    match_score = 6
            case "C":
                if shape_score == 1:
                    match_score = 6
                elif shape_score == 2:
                    match_score = 0
                else:
                    match_score = 3
        total+=match_score + shape_score

    return total

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()