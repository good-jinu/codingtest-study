cnt = 0
X = int(input())

if X < 100 :
    cnt = X
else :
    cnt = 99
    for i in range(100, X+1):
        s = str(i)
        if (int(s[0]) - int(s[1])) == (int(s[1]) - int(s[2])) :
            cnt += 1

print(cnt)


