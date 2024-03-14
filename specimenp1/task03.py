word = input()
ans = word
while len(ans) < 31:
    ans = str(ans) + str(word)
print (ans)
