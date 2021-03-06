# 직사각형에서 탈출
[문제링크](https://www.acmicpc.net/problem/1085)

## 1. 문제 설명

### 1.1 문제요약
- 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
- 제한 조건:<br> 
1 ≤ w, h ≤ 1,000<br>
1 ≤ x ≤ w-1<br>
1 ≤ y ≤ h-1<br>
x, y, w, h는 정수
### 1.2 입출력 방식 
- 첫째 줄에 x, y, w, h가 주어진다.
- 첫째 줄에 문제의 정답을 출력한다.


### 1.3 입출력 예시
- 입력 :
<br> 6 2 10 3
- 출력 : 
<br> 1

## 2. 문제해결 아이디어

### 2.1 직사각형의 경계에 닿는 케이스를 두가지로 나눠서 생각한다.
- 첫번째 케이스로 x가 w가되거나 y좌표가 h가 되면 경계선에 닿는다. x와 y가 각각 w와 h에 닿으려면 w-x, h-y 만큼의 거리만큼 이동해야한다. 
- 두번째 케이스로 x나 y좌표 둘중 하나가 0이되면 된다.
- 위의 두 개의 케이스를 모두 구한다음 그중에서 최소값을 찾으면 문제의 답이다.