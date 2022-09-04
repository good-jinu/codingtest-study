# 10845. 큐

### [문제](https://www.acmicpc.net/problem/10845)

정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

- push X: 정수 X를 큐에 넣는 연산이다.
- pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 큐에 들어있는 정수의 개수를 출력한다.
- empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
- front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

### 입력

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

```
#입력 예시
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
```

### 출력

출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

```
#출력 예시
1
2
2
0
1
2
-1
0
1
-1
0
3
```

### 풀이

큐 맛보기!

collections 패키지의 deque 기능은 일반적인 리스트와 비슷하다. 

선입선출 개념을 쓰기 위한 popleft(), appendleft(), extendleft()가 있다. 이것들을 사용하면 deque의 왼쪽에다가 해당 작업을 할 수 있다.

maxlen() 을 통해 최대 길이를 지정해줄 수 있다. 이로써 deque가 일정 길이를 넘어가면 자동으로 맨 처음 들어온 친구가 deque에서 빠지게 된다.

리스트와 달리 rotate() 를 통해 특정 인덱스 기준으로 재정렬하는 기능도 있다. 리스트였다면 슬라이싱해서 다시 붙여줘야 할텐데, 참 편하다.  

```python
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
```
