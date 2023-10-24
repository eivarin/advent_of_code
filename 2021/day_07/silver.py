f = open("input.txt")
ls = [int(x) for x in f.read().splitlines()[0].split(",")]

bot = min(ls)
top = max(ls)
results = []
for i in range(bot,top+1):
    results.append(0)
    for x in ls:
        results[i-bot] += abs(x-i)
min_value = min(results)
min_index=results.index(min_value)
print(min_value)
