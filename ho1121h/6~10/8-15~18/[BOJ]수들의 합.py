import sys
#########################
# 1 부터 더하기 시작 하므로 200에 도달할 때 까지 최대값을 구하라는 뜻
# 1 부터 n 까지 합의 공식 = n*(n+1)/2
#########################
S = int(sys.stdin.readline()) # 200
n = 1
while n*(n+1)/2 <= S:
    n+=1
print(n-1)
