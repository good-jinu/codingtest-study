# [BOJ] 11659_구간 합 구하기 4

문제 링크 : https://www.acmicpc.net/problem/11659

----------------------
## 문제 요약
  - 주어진 N개의 수 중에서 i번째부터 j번째까지의 수의 합을 출력하는 문제

## 접근 방식
  - i번째에서 j번째까지의 수의 합 = 1번부터 j번까지의 수의 합 - 1번부터 i-1번까지의 수의 합 (i>1)
