# [BOJ] 12886_돌 그룹

문제 링크 : https://www.acmicpc.net/problem/12886

-----------------------
## 문제 요약
  - 돌은 세 그룹으로 나누어져 있다.
  - X < Y인 두 돌 그룹에서 단계를 진행하면 X+X, Y-X인 두 돌 그룹으로 변경된다.
  - 세 그룹의 돌의 개수가 같게 만들 수 있으면 1, 아니면 0을 출력하는 문제

## 접근 방식
  - 돌의 총 개수가 바뀌지는 않음 => 3차원으로 생각해야 할 문제를 2차원으로 생각 가능
  - A, B의 개수를 알면 나머지 C의 개수는 총 개수에서 A, B를 빼준 값이 된다.
