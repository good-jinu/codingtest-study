import sys

input = sys.stdin.readline


target = int(input())
ans = 0

primeNum = [2, 3]
nextnum = 5

firstNumPtr = 0
lastNumPtr = 1

isLast = True

curnum = 2

def is_prime(num):
    sqt = int(num ** 0.5)
    for d in primeNum:
        if d > sqt:
            break
        if num % d == 0:
            return False
    return True

if target <= 2:
    print(target - 1)
else:
    while firstNumPtr <= lastNumPtr:
        if isLast:
            curnum += primeNum[lastNumPtr]
        else:
            curnum -= primeNum[firstNumPtr - 1]
        
        if curnum == target:
            ans += 1
        
        if curnum >= target:
            firstNumPtr += 1
            isLast = False
        else:
            noMore = True
            for n in range(primeNum[lastNumPtr] + 2, target - curnum + 1, 2):
                if is_prime(n):
                    primeNum.append(n)
                    noMore = False
                    break
            if noMore:
                firstNumPtr += 1
                isLast = False
            else:
                lastNumPtr += 1
                isLast = True
    if primeNum[lastNumPtr] != target:
        if is_prime(target):
            ans += 1
                
    print(ans)