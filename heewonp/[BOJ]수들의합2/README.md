# [수들의합2](https://www.acmicpc.net/problem/2003)
---
## 문제 요약
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

## 문제유형
투포인터

## 아이디어
1. start, end 라는 두개의 포인터를 사용
2. start는 앞부분 end는 뒷부분을 가르킴
3. 부분합 배열의 합 < 구해야 하는값
    end를 오른쪽으로 한칸 이동
   부분합 배열의 합 >= 구해야 하는값
    start를 오른쪽으로 한칸 이동
