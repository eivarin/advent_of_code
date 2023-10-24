day, year, part = (7, 2022, "a")

def solve(input):
    lns = input.split("\n")
    limit=100000
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

    result = 0
    for d in dirs:
        size = dirs[d][1]
        if size <= limit:
            result+=size
    return result

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()