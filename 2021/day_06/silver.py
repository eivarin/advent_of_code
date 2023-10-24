f = open("input.txt")
ls = [int(x) for x in f.read().splitlines()[0].split(",")]
for day in range(256):
    print(day)
    n_lanterns = len(ls)
    i=0
    while i<n_lanterns:
        if ls[i] == 0:
            ls[i] = 6
            ls.append(8)
        else:
            ls[i] -= 1
        i+=1
print(len(ls))