# [ETC] DOUBLE SQUARES

문제링크: [https://www.facebook.com/codingcompetitions/hacker-cup/2011/qualification-round/problems/A](https://www.facebook.com/codingcompetitions/hacker-cup/2011/qualification-round/problems/A)

## 🔍 문제분석

- 주어진 정수 X를 두개의 완전 제곱수의 합으로 나타내어야 한다.
- 나타낼 수 있는 경우의 수를 출력한다.

예시)

```
10 = 1 * 1 + 3 * 3

25 = 0 * 0 + 5 * 5
25 = 3 * 3 + 4 * 4
```

## 💡 아이디어

1. 완전제곱수 집합을 구한다.

```
squreset = {0, 1, 4, 9, 16, 25, 36, 49, 64, ...}
```

2. 주어진 수에 완전제곱수를 순차적으로 뺄셈을 한다.

```
X = 25

X - 0 = 25
X - 1 = 24
X - 4 = 21
X - 9 = 16
X - 16 = 9
X - 25 = 0
```

3. 뺄셈을 해서 나온 수가 완전제곱수 집합에 존재한다면 그 경우의 수를 카운트한다.(중복되는 경우의 수는 제외)