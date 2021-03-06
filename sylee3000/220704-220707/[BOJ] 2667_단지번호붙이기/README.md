# [BOJ] 2667_단지번호붙이기

문제 링크 : https://www.acmicpc.net/problem/2667

-------------------
## 문제 요약
  - 1로 연결되어 있는 집들을 하나의 단지로 가정
  - 단지의 개수를 출력한 후 단지 내의 집의 수를 오름차순으로 출력하는 문제

## 접근 방식
  - BFS 사용
  - N x N의 지도를 돌면서 1을 찾으면 그 위치부터 BFS 수행, 
  - 한 칸 지나갈 때마다 count를 1 증가, 방문한 위치의 값은 0으로 변경
  - 더 이상 방문할 칸이 없을 때의 count를 저장
  - 지도의 모든 칸을 방문 완료했을 때 저장한 count 값의 개수가 단지의 개수가 되고, 각각의 단지 내의 집의 수는 count 리스트를 오름차순하면 된다.
