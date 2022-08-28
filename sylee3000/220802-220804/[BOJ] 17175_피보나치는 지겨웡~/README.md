# [BOJ] 17175_피보나치는 지겨웡~

문제 링크 : https://www.acmicpc.net/problem/17175

--------------------
## 문제 요약
  ![image](https://user-images.githubusercontent.com/102509777/182503695-1a07a09a-ec2a-43c3-a0c8-c7ef8d849d5f.png)
  - 위와 같은 코드가 있을 때 입력으로 fibonacci(n)이 들어온다면 함수가 호출되는 횟수가 몇 번인지 출력하는 문제

## 접근 방식
  - n이 0, 1일 때는 함수는 한 번만 호출
  - n이 2 이상일 때는 n 호출(=1) + (n-2) 호출 + (n-1) 호출
