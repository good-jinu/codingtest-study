# [BOJ] 15927_회문은 회문아니야!!

문제 링크 : https://www.acmicpc.net/problem/15927

--------------------
## 문제 요약
  - 알파벳 대문자로 이루어진 문자열이 주어졌을 때, 팰린드롬이 아닌 가장 긴 부분문자열의 길이를 구하는 문제
  - 이때 부분문자열을 이루는 글자는 연속해야 한다. AB는 ABCD의 부분문자열이지만, AC는 아니다.

## 접근 방식
  - ad hoc
  - 모든 문자가 같은 영단어로 이루어져있으면 부분문자열들도 항상 팰린드롬이기 때문에 -1을 출력
  - 주어진 문자열이 팰린드롬이 아니라면 가장 긴 부분문자열은 그대로 주어진 문자열이 된다.
  - 주어진 문자열이 팰린드롬이라면 가장 긴 부분문자열은 주어진 문자열에서 알파벳 하나가 빠진 문자열이 된다.
