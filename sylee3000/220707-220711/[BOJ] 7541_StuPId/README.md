# [BOJ] 7541_StuPId

문제 링크 : https://www.acmicpc.net/problem/7541

------------------
## 문제 요약
  - 6자리 또는 7자리의 숫자의 각 자리수에 역순으로 9, 3, 7을 곱한 값을 모두 더한 값의 일의 자리가 0이 되어야 유효한 id이다.
  - id 중 한 자리의 값이 ?로 주어질 때, ?의 값을 찾아 출력하는 문제

## 접근 방식
  - 입력받은 id를 역순으로 변경
  - 각 자리수가 ?이면 그 당시에 곱해주어야 할 값을 저장, 아니면 checksum에 곱한 값을 더해준다.
  - 모든 자리수의 처리를 완료했으면 다시 id를 기존 순서대로 변경
  - 조건을 만족하는 수 i를 찾았으면 ?를 i로 변경해준 뒤 출력
