day, year, part = (11, 2022, "b")

def solve(input):
    lns = input.splitlines()
    class Monkey:
        def __init__(self, items, operation, test, trueMonkey, falseMonkey):
            self.items = items
            self.operation = operation
            self.test = test
            self.trueMonkey = trueMonkey
            self.falseMonkey = falseMonkey
            self.count = 0

        def __repr__(self) -> str:
            return f"items:{self.items},operation:{self.operation},test:{self.test},true:{self.trueMonkey},false={self.falseMonkey}\n"
        
        def takeTurn(self,ms):
            l = []
            for old in self.items:
                l.append(eval(self.operation, {"old":old}))
                self.count+=1
            # print(l)
            l = list(map(lambda old: old%9699690, l))
            # print(l)
            # print("-")
            for it in l:
                if it % self.test == 0:
                    ms[self.trueMonkey].items.append(it)
                else:
                    ms[self.falseMonkey].items.append(it)
            self.items = []
            return ms

    monkeys = []
    items = []
    operation = ""
    test = 0
    trueMonkey = 0
    falseMonkey = 1
    for l in lns:
        lsp = l.split()
        if l != "":
            match lsp[0]:
                case "Starting":
                    items = [int(x) for x in l.split(":")[1].split(",")]
                case "Operation:":
                    operation = l.split("=")[1]
                case "Test:":
                    test = int(lsp[-1])
                case "If":
                    if lsp[1] == "true:":
                        trueMonkey = int(lsp[-1])
                    else:
                        falseMonkey = int(lsp[-1])
        else:
            new_monkey = Monkey(items,operation,test,trueMonkey, falseMonkey)
            monkeys.append(new_monkey)
    else:
        new_monkey = Monkey(items,operation,test,trueMonkey, falseMonkey)
        monkeys.append(new_monkey)
    i = 0
    while i<10000:
        t = 0 
        while t<len(monkeys):
            monkeys = monkeys[t].takeTurn(monkeys)
            t+=1
        i+=1

    result = []
    for m in monkeys:
        result.append(m.count)
    result.sort()

    return result[-1] * result[-2]

import aocd
def main():
    data = aocd.get_data(day=day, year=year)
    result = solve(data)
    print(f"============ Trying Submiting! ============\nCurrent Result: {result}")
    aocd.submit(result, day=day, year=year, part=part)

if __name__ == "__main__":
    main()