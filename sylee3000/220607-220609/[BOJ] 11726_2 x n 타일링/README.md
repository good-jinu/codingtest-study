# [BOJ] 11726_2 x n 타일링

문제 링크 : https://www.acmicpc.net/problem/11726

-----------------
## 문제 요약
  - 1x2 타일과 2x1 타일을 사용하여 2xn 크기의 직사각형을 채우는 방법의 개수를 구하는 문제

## 접근 방식
  - 다이나믹 프로그래밍 이용
  - 2xn 크기의 직사각형을 채우는 방법은 가장 오른쪽에 세로 타일을 넣었을 때와 가로 타일을 2개 넣었을 때로 나눌 수 있다.
  - 세로 타일을 넣으면 2x(n-1) 크기의 직사각형을 채우는 방법의 개수, 가로 타일 2개를 넣으면 2x(n-2) 크기의 직사각형을 채우는 방법의 개수만큼 가능하다.
  - f(n) = f(n-1) + f(n-2) (f(1)=1, f(2)=2)
