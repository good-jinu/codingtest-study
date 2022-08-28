import sys
x,y,w,h = map(int,sys.stdin.readline().split())
mix_d = [x,y,w-x,h-y]
print(min(mix_d))