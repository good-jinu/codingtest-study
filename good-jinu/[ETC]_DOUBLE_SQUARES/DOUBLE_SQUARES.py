import sys

input = sys.stdin.readline

squareset = set([])

for i in range(46341):
    squareset.add(i*i)

T = int(input())

for i in range(T):
    cnt = 0
    num = int(input())
    usedset = set()
    for j in range(46341):
        square1 = j * j
        if square1 > num:
            break
        if square1 in usedset:
            continue
        square2 = num - square1
        if square2 in squareset:
            cnt += 1
            usedset.add(square2)
    print(f'Case #{i+1}: {cnt}')