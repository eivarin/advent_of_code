f = open("input.txt")
lns= [l.split() for l in f.readlines()]
movements = [(direction, int(value)) for direction, value in lns]

x = 0
y = 0

for direction, value in movements:
    match direction:
        case "up":
            y-=value
        case "down":
            y+=value
        case "forward":
            x+=value

result = x*y
print(result)