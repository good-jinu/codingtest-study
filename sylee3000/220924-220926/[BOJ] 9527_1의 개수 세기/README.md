# [BOJ] 9527_1의 개수 세기

문제 링크 : https://www.acmicpc.net/problem/9527

--------------------
## 문제 요약
  - A부터 B까지의 수를 이진법으로 나타냈을 때 1의 총 개수를 구하는 문제

## 접근 방식
![1의 개수 세기](https://user-images.githubusercontent.com/102509777/192031260-7bc28d55-fcac-4628-a9e4-706cf03a8eb6.JPG)
  - 색이 같은 박스는 같은 값을 나타낸다.
  - ex) 5~7은 1~3에 4(이진법으로 100)를 추가한 값
  - 따라서 1에서 2 ** n - 1까지의 수의 1의 개수의 합 = 2 ** (n-1) + 2 * (1에서 2 ** (n-1) - 1까지의 수의 1의 개수의 합)이 된다.
