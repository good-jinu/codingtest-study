# [BOJ] 10775_공항

문제 링크 : https://www.acmicpc.net/problem/10775

--------------------
## 문제 요약
  - 비행기를 도킹할 수 있는 게이트의 범위가 입력으로 주어진다.
  - 한 게이트에는 비행기가 한 대만 도킹이 가능하다.
  - 어느 한 비행기가 도킹이 불가능하다면 그대로 공항이 폐쇄되어 나머지 비행기는 도킹할 수 없다.
  - 이때, 도킹이 가능한 비행기의 대수를 구하는 문제이다.

## 접근 방식
  - 그리디 문제
  - 게이트의 범위가 주어지면 가장 큰 수부터 비행기가 있는지 확인해서 없으면 그곳에 비행기를 도킹시킨다.
