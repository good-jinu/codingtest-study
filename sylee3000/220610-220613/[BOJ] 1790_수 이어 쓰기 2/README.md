# [BOJ] 1790_수 이어 쓰기 2

문제 링크 : https://www.acmicpc.net/problem/1790

-------------------------------
## 문제 요약
  - 1부터 N까지의 수를 한 줄로 이어 붙인 수에서 앞에서 k번째 자리의 수가 무엇인지 출력하는 문제

## 접근 방식
  - 먼저 앞에서 k번째 위치의 이어붙이기 전 숫자를 구해준다.
    - 1~9 : 길이 1, 개수 9 / 10~99 : 길이 2, 개수 90 / 100~999 : 길이 3, 개수 900 / ...
    - 길이가 늘어날 때마다 개수가 10배로 늘어남
    - 길이를 먼저 구한 뒤 숫자를 구해준다.
  - k-1을 길이 l로 나눈 나머지를 인덱스로 설정해 준 뒤 위에서 구한 숫자에서 인덱스 값에 해당하는 수를 출력해준다.
    - 만약 구한 숫자가 N보다 클 때는 -1을 출력한다.
