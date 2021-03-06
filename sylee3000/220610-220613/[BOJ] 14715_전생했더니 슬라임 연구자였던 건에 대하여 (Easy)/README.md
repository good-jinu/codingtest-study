# [BOJ] 14715_전생했더니 슬라임 연구자였던 건에 대하여 (Easy)

문제 링크 : https://www.acmicpc.net/problem/14715

-----------------
## 문제 요약
  - 초기 슬라임은 흠집이 0개이다.
  - 슬라임 에너지가 K인 슬라임은 A * B = K (A, B는 2 이상인 자연수)일 때 슬라임 에너지가 A인 슬라임과 B인 슬라임으로 분할할 수 있다. 
  - 흠집이 T개인 슬라임이 분할되면 분할된 두 슬라임은 T+1개의 흠집을 갖게 된다.
  - 모든 슬라임들이 더 이상 분할되지 못할 때 흠집을 가장 많이 가지는 슬라임의 흠집 개수의 최소값을 구하는 문제

## 접근 방식
  - 더 이상 분할되지 못하는 슬라임들의 슬라임 에너지는 소수이다.
  - 먼저 입력받은 K를 소인수분해하고, 소수의 총 개수 count를 구한다.
  - log2(count)를 올림해준 값이 답이 된다.
