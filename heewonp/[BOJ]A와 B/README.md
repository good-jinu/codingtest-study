# [문서 검색](https://www.acmicpc.net/problem/12904)
---
## 문제 요약
수빈이는 A와 B로만 이루어진 영어 단어가 존재한다는 사실에 놀랐다. 대표적인 예로 AB (Abdominal의 약자), BAA (양의 울음 소리), AA (용암의 종류), ABBA (스웨덴 팝 그룹)이 있다.

이런 사실에 놀란 수빈이는 간단한 게임을 만들기로 했다. 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.

문자열의 뒤에 A를 추가한다.
문자열을 뒤집고 뒤에 B를 추가한다.
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 

## 문제유형
그리디

## 아이디어
1. T가 마지막 글자가 A일 경우 마지막 글자 제거 
2. 그렇지 않을 경우 T마지막 글자 제거 후, 문자열을 뒤집어 줌
3. 만약 S와 T가 같을 경우 가능 그렇지 않을 경우 불가능

## 주의할 점
S가 T가 되는지 확인하면 시간오류, T가 S가 되는지 역으로 생각 해볼것
