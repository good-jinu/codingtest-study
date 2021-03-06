## 수들의 합
[문제링크](https://www.acmicpc.net/problem/1789)

![수들의 합](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%88%98%EB%93%A4%EC%9D%98%ED%95%A9.JPG?raw=true)
<br>
그림과 같이 10에서 14까지는 서로 다른 4개(1+2+3+4)의 자연수의 합에서 4가 최댓값이 된다.
<br>
15부터는 1+2+3+4+5=15라서 5를 최댓값으로 가지며 20까지 동일하고, 21부터 1+2+3+4+5+6=21으로 6이 최댓값이 된다.
<br>
따라서 예제와 같이 200을 입력하면 최대값이 19가 되게하는 코드를 작성해야 한다.
<br>
이 문제를 해결하기 위한 접근으로, 먼저 높은 수를 입력했을 때와 이에 대한 최대값 계산을 반복적으로 하기 위해 while 문을 사용하였으며, N을 1부터 시작해서 자연수의 합 S를 빼서 N값이 S값보다 커질 때에는 그때의 N값이 최댓값이 되는 것을 확일할 수 있다. 그렇지 않을 때에는 N값을 1씩 증가시키면서 이 과정을 반복하게 된다.