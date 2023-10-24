day, year, part = (7, 2022, "b")

def solve(input):
    lns = input.split("\n")
    dirs = {}
    curr_dir = ""
    for l in lns:
        l = l.split()
        if l[0] == "$":
            match l[1]:
                case "cd":
                    path = curr_dir + l[2] if curr_dir == "/" else f"{curr_dir}/{l[2]}"
                    if l[2] == "..":
                        curr_dir = dirs[curr_dir][-1]
                    elif l[2] == "/":
                        if "/" not in dirs:
                            dirs["/"] = ["/",0,[],[],""]
                        curr_dir="/"
                    elif path in dirs:
                        curr_dir = dirs[path]
                    else:
                        dirs[path] = [path,0,[],[],curr_dir]
                        curr_dir=path
                case "ls":
                    pass
        elif l[0] == "dir":
            dirs[curr_dir][2].append(l[1])
        else:
            dirs[curr_dir][3].append((l[1],l[0]))
            size=int(l[0])
            dirs[curr_dir][1]+=int(l[0])
            d = curr_dir
            while dirs[d][-1] != "":
                d = dirs[d][-1]
                dirs[d][1]+=size


    l = []
    for d in dirs:
        l.append((dirs[d][1],dirs[d][0]))

    l.sort(key=lambda d: d[0])

    needed_space = 30000000 - (70000000 - l[-1][0])
    result = 0
    for d in l:
        result = d[0]
        if d[0] > needed_space:
            break
    return result

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()