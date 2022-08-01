import math
import sys
 
input = sys.stdin.readline
 
n = int(input())
 
 
def is_prime_num(num): # 소수 판별 함수.
    if num == 0 or num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
 
 
p_num = []
i = 2
while True:
	if len(p_num) == 2: # 2개가 되면 작동.
		if p_num[0] * p_num[1] > n:
			print(p_num[0] * p_num[1]) # N보다 크면서 연속된 두 소수의 합
			break
		else:
			p_num.pop(0) #두개의 합이 N보다 작으면 앞에꺼버려준다.
	if is_prime_num(i): # 소수인것들 넣음 2부터 증가시키면서 
		p_num.append(i) # P_num에 넣어준다.
	i += 1

