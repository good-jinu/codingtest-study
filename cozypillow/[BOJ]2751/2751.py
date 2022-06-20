# 입력
import sys
input = sys.stdin.readline
test = input()
print(test)
N = int(input())

num_list = []
for i in range(N):
    num_list.append(int(input()))

# 정렬
num_list = sorted(num_list)


# 출력
for num in num_list:
    print(num)
