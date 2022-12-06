f = open("input.txt")

lns = f.read().splitlines()
total=0
for l in lns:
    plays = l.split()
    p1, p2 = plays
    shape_score = 0
    match_score = 0
    match p2:
        case "X":
            match_score = 0
        case "Y":
            match_score = 3
        case "Z":
            match_score = 6
    match p1:
        case "A":
            if match_score == 0:
                shape_score = 3
            elif match_score == 3:
                shape_score = 1
            else:
                shape_score = 2
        case "B":
            if match_score == 0:
                shape_score = 1
            elif match_score == 3:
                shape_score = 2
            else:
                shape_score = 3
        case "C":
            if match_score == 0:
                shape_score = 2
            elif match_score == 3:
                shape_score = 3
            else:
                shape_score = 1
    total+=match_score + shape_score

print(total)
    