# [BOJ] 4811_알약

문제 링크 : https://www.acmicpc.net/problem/4811

-------------------
## 문제 요약
  - 약은 무조건 반 조각씩만 먹어야함
  - 한 조각을 꺼냈으면 나머지 반 조각은 다시 병에 넣는다.
  - 한 조각을 꺼냈으면 W, 반 조각을 꺼냈으면 H
  - 가능한 문자열의 개수를 구하는 문제

## 접근 방식
  - DP
  - ![image](https://user-images.githubusercontent.com/102509777/184557810-f5d68752-ce46-4cdb-b1c5-eecdce7af250.png)
  - dp[W][H] = dp[W][H-1] + dp[W-1][H]
  - W가 0이면 모두 H이기 때문에 1가지 방법만 존재
  - W == H+1이면 H가 하나도 존재하지 않는다는 것이기 때문에 dp[W][H] = dp[W-1][H-1] + dp[W-1][H]로 계산
