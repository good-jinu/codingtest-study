# [BOJ] 2606_바이러스

문제 링크 : https://www.acmicpc.net/problem/2606

-----------------
## 문제 요약
  - 네트워크 상으로 연결되어 있을 때 한 컴퓨터가 바이러스에 감염되면 나머지 컴퓨터들도 바이러스가 감염됨
  - 1번 컴퓨터가 바이러스에 감염되었을 때 바이러스에 감염되는 컴퓨터들의 개수를 구하는 문제

## 접근 방식
  - BFS
  - 감염되지 않았는데 감염된 컴퓨터와 연결되어 있으면 감염됨
