# [BOJ] 10845_큐

문제 링크 : https://www.acmicpc.net/problem/10845

-------------------
## 문제 요약
  - 큐를 구현하는 문제
  1. push X: 정수 X를 큐에 넣는 연산이다.
  2. pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
  3. size: 큐에 들어있는 정수의 개수를 출력한다.
  4. empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
  5. front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
  6. back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

## 접근 방식
  - 리스트 이용
  - 여러줄의 입력을 받아야하기 때문에 sys.stdin.readline으로 시간 줄이기
