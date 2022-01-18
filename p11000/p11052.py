# coding=utf-8

'''카드 구매하기
https://www.acmicpc.net/problem/11052
'''

import sys
input = sys.stdin.readline

N = int(input())
ps = list(map(int, ('0 '+input()).split()))

mxs = [0] * (N+1)
for i in range(1, N+1):
    mx = ps[i]
    for j in range(1, (i//2)+1):
        mx = max(mxs[i-j] + mxs[j],  mx)
    mxs[i] = mx

print(mxs[N])

# pass

# 다이나믹 프로그래밍