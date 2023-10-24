f = open("input.txt")
ls = [int(x) for x in f.read().splitlines()[0].split(",")]

bot = min(ls)
top = max(ls)
results = []
for i in range(bot,top+1):
    print(i)
    results.append(0)
    for x in ls:
        results[i-bot] += sum(range(1,abs(x-i) + 1))
min_value = min(results)
min_index=results.index(min_value)
print(min_value)