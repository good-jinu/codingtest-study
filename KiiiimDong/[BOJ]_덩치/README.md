# 덩치
[문제링크](https://www.acmicpc.net/problem/7568)

## 1. 문제 설명

### 1.1 문제요약
- 우리는 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다. 어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다.
- 어떤 사람보다 덩치가 크다의 기준은 몸무게와 키가 동시에 클 때만 성립한다.
- 이때 사람들의 몸무게와 덩치가 주어질 때 덩치 순위를 매겨라.
- 덩치 비교가 불가능한 사람들은 같은 등수로 취급한다.(A와 B를 비교했을 때 A는 B보다 키가 크지만 , 몸무게는 A가 더 작은 경우 혹은, 몸무게는 더 크지만 키가 더 작은경우)

### 1.2 입력 방식 
- 첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

### 1.3 입출력 예시

- 입력:
- 5
- 55 185
- 58 183
- 88 186
- 60 175
- 46 155
- 출력 : 2 2 1 2 5

## 2. 문제해결 아이디어

### 2.1 덩치 비교가 가능한 단 하나의 방식
- 키와 몸무게가 둘다 커야만 덩치가 크다고 얘기할 수 있다. 이 경우를 제외하고는 덩치를 서로 비교할 수 없다.

### 2.2 위의 단 하나의 방식만 카운트
- 위에서 말한 단 하나의 방식만 카운트하기 위해서 덩치비교가 가능한 케이스만 카운트해서 덩치가 작은사람의 등수를 한칸씩 밀려나게하는 방식으로 카운트한다.


## 3. 자주 이용하지 않아서 헷갈렸던 개념
- sep=" " 
print문의 출력문들 사이에 해당하는 내용을 넣을 수 있다. 기본 값으로는 공백이 들어가 있으며 이를 사용해 원하는 문자를 입력할 수 있다.
- end=" "
print 문을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있다. 기본 값으로는 개행(\n)이 들어가 있으며 이를 사용해 개행을 없애거나 원하는 문자를 입력할 수 있다. 