# 전체 계산 횟수
[문제링크](https://www.acmicpc.net/problem/17174)
> 수학, 사칙연산을 이용한 문제
### 아이디어
> 모든 돈을 1달러화, 처음달러세고시작 ,총 n달러를 m개씩 묶음, 묶음들을 m개씩 다시 묶음 세기 
>> 입력 넣은 N값을 다른 객체에 넣어서 처음 총달러수 세기
>> 한묶음당 계산시 총N값에서 제외해주며 묶음을 세기는것을 +=1로 묶음이 늘어가는 것을 저장
>> 묶음들이 M개가 되었을시 묶음을 해주므로 count+1해준다.