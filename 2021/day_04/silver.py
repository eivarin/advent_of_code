f = open("input.txt")
lns= f.read().splitlines()

magic_numbers = [int(n) for n in lns[0].split(",")]
drawn_numbers = []
def check_bingo(card):
   _, columns, lines, diags = card
   for v in columns+lines+diags:
       if v == 0:
           break

cards =[[[],{},[5,5,5,5,5],[5,5,5,5,5],[5,5],set()]]
def print_card(c):
    print("board:")
    for i in range(5):
        print(cards[0][i])
    print(f"\ncoords:{c[1]}")
    print(f"cols:{c[2]}")
    print(f"lines:{c[3]}")
    print(f"diags:{c[4]}")
    print(f"not visited:{c[5]}")

i = 0
x=0
y=0
for l in lns[1:]:
   if l != "":
       l = [int(n) for n in l.split()]
       cards[i][0].append(l)
       for e in l:
           cards[i][-1].add(e)
           cards[i][1][e] = (x,y)
           x+=1
       x=0
       y+=1
   else:
       cards.append([[],{},[5,5,5,5,5],[5,5,5,5,5],[5,5],set()])
       y=0
       i+=1

def check_win(c):
   for col in c[2] + c[3] + c[4]:
    #    print(col)
       if col == 0:
           return True

def mark_number(c, n):
   x, y = c[1][n]
   c[-1].remove(n)
   c[2][x]-=1
   c[3][y]-=1
#    if (x, y) in [(0,0),(1,1),(2,2),(3,3),(4,4)]:
#        c[4][0]-=1
#    if (x, y) in [(0,4),(1,3),(2,2),(3,1),(4,0)]:
#        c[4][1]-=1
   return c

winners = ([],[])
for n in magic_numbers:
    for c in cards:
        if n in c[-1]:
            c = mark_number(c, n)
            if check_win(c):
                winners[0].append(c)
                winners[1].append(c)
    print(n)
    if n == 24:
        print(cards[2])
    cards = list(filter(lambda c: c not in winners[0], cards))
    if len(winners[0]) > 0:
        print_card(winners[0][0])
        break

soma_unchecked = sum(winners[0][0][-1])
result = soma_unchecked * n
print(result)