# 5와 6의 차이
[문제링크](https://www.acmicpc.net/problem/2864)

## 1. 문제 설명
### 1.1 문제요약
- 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.
- 두 수 A와 B가 주어졌을 때, 두 수의 가능한 합 중, 최솟값과 최댓값을 구하라.
### 1.2 입출력 예시
- 11 25 -> 36 37
- 1430 4862 -> 6282 6292

## 2. 문제해결 아이디어
### 2.1 5와 6
- 문제의 핵심은 5와 6을 헷갈려서 5와 6을 보게되면 어느것이 나와도 이상하지 않다는 것이다.
- 따라서 5와 6을 봤을 때 그 숫자를 어떻게 5와 6중 어느 것으로 처리하느냐가 이 문제의 핵심아이디어다.

### 2.2 최소값과 최대값
- 두 숫자의 합의 최대값과 최소값을 구하는 문제인데, 5와 6을 바꿔서 최대와 최소를 가를 수 있다.
- 숫자안에 5나 6이 있을 때 그 숫자들을 모두 6으로 바꿔서 더하면 최대값, 모두 5로 바꿔서 더하면 최소값을 가진다.
