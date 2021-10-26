# coding=utf-8
'''덩치
https://www.acmicpc.net/problem/7568
'''
import sys
input = sys.stdin.readline

N = int(input())
xys = []
for _ in range(N):
    xy = tuple(map(int, input().split()))
    xys.append(xy)

rank = [None]*N
for i in range(N):
    gn = 0
    for j in range(N):
        if i != j:
            if xys[i][0] < xys[j][0] and xys[i][1] < xys[j][1]:
                gn += 1
    rank[i] = str(gn+1)

print(' '.join(rank))

# pass

# 브루트포스_알고리즘