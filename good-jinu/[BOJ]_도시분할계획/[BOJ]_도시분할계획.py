import sys

input = sys.stdin.readline

N, M = map(int, input().split())

unions = [i for i in range(N + 1)]

roads = [tuple(map(int, input().split())) for _ in range(M)]
roads.sort(key=lambda x: x[2])

ans = roads[0][2]

def makeUnion(a, b): # if two are already union return true
    aroot = a
    while unions[aroot] != aroot:
        aroot = unions[aroot]
    broot = b
    while unions[broot] != broot:
        broot = unions[broot]
    if aroot == broot:
        return True
    else:
        if aroot > broot:
            unions[aroot] = broot
        else:
            unions[broot] = aroot
        return False

makeUnion(roads[0][0], roads[0][1])
lasti = 0

for i in range(1, M):
    if makeUnion(roads[i][0], roads[i][1]):
        continue
    ans += roads[i][2]
    lasti = i

ans -= roads[lasti][2]

print(ans)
