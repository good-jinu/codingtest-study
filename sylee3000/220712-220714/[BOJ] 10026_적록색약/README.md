# [BOJ] 10026_적록색약

문제 링크 : https://www.acmicpc.net/problem/10026

----------------
## 문제 요약
  - 적록색약인 사람은 빨강과 초록을 비슷하게 본다.
  - 주어진 그림을 일반 사람과 적록색약인 사람이 몇개의 부분으로 인식할 지를 구하는 문제
  
## 접근 방식
  - 먼저 일반 사람 기준으로 BFS 진행
  - 그림에서 G를 R로 변경
  - 적록색약인 사람 기준으로 BFS 진행
