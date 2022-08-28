## 직사각형에서 탈출
[문제링크](https://www.acmicpc.net/problem/1085)

![직사각형에서 탈출](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%EC%97%90%EC%84%9C%20%ED%83%88%EC%B6%9C.JPG?raw=true)
![직사각형에서 탈출2](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%EC%97%90%EC%84%9C%20%ED%83%88%EC%B6%9C2.JPG?raw=true)
![직사각형에서 탈출3](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%EC%97%90%EC%84%9C%20%ED%83%88%EC%B6%9C3.JPG?raw=true)

```python
import sys
x,y,w,h = map(int,sys.stdin.readline().split())
mix_d = [x,y,w-x,h-y]
print(min(mix_d))
```