import sys
from collections import deque

input = sys.stdin.readline

q = deque()
n = int(input())

for i in range(n):
    action = input()       
    if action.split()[0] == "push":
        q.append(action.split()[1])
    elif action == "pop\n":
        if len(q) == 0:
            print(-1)
        else:
            pop = q.popleft()
            print(pop)
    elif action == "size\n":
        print(len(q))
    elif action == "empty\n":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif action == "front\n":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif action == "back\n":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
