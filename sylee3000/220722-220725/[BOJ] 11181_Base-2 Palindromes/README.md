# [BOJ] 11181_Base-2 Palindromes

문제 링크 : https://www.acmicpc.net/problem/11181

-------------------
## 문제 요약
  - 2진수로 변환했을 때 팰린드롬이 되는 수 중 크기가 N번째로 큰 수를 구하는 문제

## 접근 방식
  - 끝자리만 겹치게 : 홀수 자리의 이진수 (ex. 1011 -> 101|1|101 => 1011101)
  - 전체 뒤집기 : 짝수 자리의 이진수 (ex. 1011 -> 1011|1101 => 10111101)

<2진수 팰린드롬>
![KakaoTalk_20220725_184559372_01](https://user-images.githubusercontent.com/102509777/180748849-216ba0ef-f3fb-4970-afec-172311156fff.jpg)



<2진수 팰린드롬 (홀수)>
![KakaoTalk_20220725_184559372_02](https://user-images.githubusercontent.com/102509777/180748902-fb854a21-c552-47c8-9291-8bc03db87926.jpg)



<2진수 팰린드롬 (짝수)>
![KakaoTalk_20220725_184559372_03](https://user-images.githubusercontent.com/102509777/180748939-911a2f74-df95-447b-bfc0-17cfd8f64ae3.jpg)
