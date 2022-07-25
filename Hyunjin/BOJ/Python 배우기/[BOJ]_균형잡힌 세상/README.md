## 균형잡힌 세상
[문제링크](https://www.acmicpc.net/problem/4949)

![균형잡힌 세상](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EA%B7%A0%ED%98%95%EC%9E%A1%ED%9E%8C%20%EC%84%B8%EC%83%81.JPG?raw=true)
![균형잡힌 세상2](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EA%B7%A0%ED%98%95%EC%9E%A1%ED%9E%8C%20%EC%84%B8%EC%83%812.JPG?raw=true)

```python
while True:
    string = input()
    stack = []

    if string == '.':
        break

    for i in string:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
```