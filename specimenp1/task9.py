dance = ['<','+','&','>']
start = input()
pos = dance.index(start)
a = 0
moves = []
ans = ''
while a < 8:
    moves.append(dance[pos])
    pos = pos + 1
    pos = pos % 4
    a = a + 8
print (moves)
for i in moves:
    ans = ans + i
print (ans)
