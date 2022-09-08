import sys
input = sys.stdin.readline

N = int(input())

ppr = [list(map(int, input().split())) for j in range(N)]

whiteblue = [0, 0]

def allequal(s, e, lst):
    for i in lst:
        if i[s] != lst[0][s]:
            return False
        if len(set(i[s:e])) > 1:
            return False
    return True

def sliceppr(s, e, s1, e1):
    mid = (e-s)//2 + s
    mid1 = (e1-s1)//2 + s1
    tmp = ppr[s:mid]
    if allequal(s1, mid1, tmp):
        whiteblue[tmp[0][s1]] += 1
    else:
        sliceppr(s, mid, s1, mid1)
    
    if allequal(mid1, e1, tmp):
        whiteblue[tmp[0][mid1]] += 1
    else:
        sliceppr(s, mid, mid1, e1)
    
    tmp = ppr[mid:e]
    if allequal(s1, mid1, tmp):
        whiteblue[tmp[0][s1]] += 1
    else:
        sliceppr(mid, e, s1, mid1)
    
    if allequal(mid1, e1, tmp):
        whiteblue[tmp[0][mid1]] += 1
    else:
        sliceppr(mid, e, mid1, e1)

if allequal(0, N, ppr):
    whiteblue[ppr[0][0]] += 1
else:
    sliceppr(0, N, 0, N)

print(whiteblue[0])
print(whiteblue[1])