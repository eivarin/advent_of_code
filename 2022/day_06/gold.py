f = open("input.txt")  
l = f.read().splitlines()[0]
i=0
n=14
while i+3<len(l):
    start = set()
    for x in range(n):
        start.add(l[i+x])
    if len(list(start)) == n:
        break
    i+=1

print(i+n)