# [BOJ] 10830_행렬 제곱

문제 링크 : https://www.acmicpc.net/problem/10830

------------------
## 문제 요약
  - 크기가 N * N인 행렬 A의 B제곱의 원소를 1000으로 나눈 나머지를 출력하는 문제

## 접근 방식
  - B가 짝수일 때는 A의 B제곱을 A의 B//2제곱을 두 번 진행하는 것으로 바꿀 수 있다.
  - B가 홀수일 때는 A의 B-1제곱과 A를 곱해준다.
