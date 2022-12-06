f = open("input.txt")
lns= [l.split() for l in f.readlines()]
movements = [(direction, int(value)) for direction, value in lns]

x = 0
my= 0
y = 0

for direction, value in movements:
    match direction:
        case "up":
            my-=value
        case "down":
            my+=value
        case "forward":
            x+=value
            y+=value*my

result = x*y
print(result)