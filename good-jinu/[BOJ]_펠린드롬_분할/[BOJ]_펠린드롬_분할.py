import sys

input = sys.stdin.readline

dp1 = [[-1 for i in range(2501)] for j in range(2501)]
dp2 = [2147483648] * 2501
dp2[0] = 0

str = "#" + input().strip()

def isPal(s, e):
    tmp = str[s:e+1]
    return tmp == tmp[::-1]

for i in range(1, len(str)):
    dp2[i] = dp2[i-1] + 1
    for j in range(1, i):
        if not isPal(j, i):
            continue
        dp2[i] = min(dp2[i], dp2[j-1] + 1)

print(dp2[len(str) - 1])