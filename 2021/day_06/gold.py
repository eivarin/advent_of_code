from functools import reduce


f = open("input.txt")
ls = [int(x) for x in f.read().splitlines()[0].split(",")]
sss = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for l in ls:
    sss[l]+=1

for day in range(1000**10):
    print(day)
    kabum_n = sss[0]
    sss[7]+= kabum_n
    for i in range(8):
        sss[i] = sss[i+1]
    sss[8] = kabum_n
print(reduce(lambda total, x: total+sss[x], sss,  0))