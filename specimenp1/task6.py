ppl = []
for i in range (5):
    h = input()
    ppl.append(h)
a = 0
while a < 5:
    if ppl[a] == 'Ellie' :
        ans = a 
    a = a + 1
    
place = ['1st','2nd','3rd','4th','5th']
ans = place [ans]
print(ans)
