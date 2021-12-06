# coding=utf-8

'''노브 돌리기
https://www.acmicpc.net/problem/23756
'''

import sys
input = sys.stdin.readline

N = int(input())
a0 = int(input())
out = 0
for _ in range(N):
    i = int(input())
    a = abs(i - a0) 
    if a>180:
        a = 360 - a
    out += a
    a0 = i

print(out)


# pass


# 수학
# 구현