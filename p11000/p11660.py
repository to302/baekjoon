# coding=utf-8

'''구간 합 구하기 5
https://www.acmicpc.net/problem/11660
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    ns = list(map(int, input().split()))
    arr.append(ns)

# make accumulated array
acc = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        acc[i][j] = arr[i-1][j-1] + acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = acc[x2][y2] - acc[x1-1][y2] - acc[x2][y1-1] + acc[x1-1][y1-1]
    print(ans)

# pass
# 
# 다이나믹 프로그래밍
# 누적 합    