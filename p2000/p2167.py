# coding=utf-8

'''2차원 배열의 합
https://www.acmicpc.net/problem/2167
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) 
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


acc = [[] for _ in range(N)]
for i in range(N):
    acc[i].append(0)
    acc[i].append(arr[i][0])
    for j in range(1, M):
        acc[i].append(acc[i][-1] + arr[i][j])


K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split()) # 좌표이용 사각형 범위 내 값을 구하기
    sm = 0
    for ix in range(i-1, x):
        sm += acc[ix][y] - acc[ix][j-1]
    print(sm)


# pass

# 누적 합
# 구현


''' 다른 사람 빠른 버전
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = []
for _ in range(N):
    a.append(list(map(int, input().split())))

dp = [[0] * (M+1) for _ in range(N+1)]
for k in range(1, N+1):
    for l in range(1, M+1):
        dp[k][l] = a[k-1][l-1] + dp[k][l-1] + dp[k-1][l] - dp[k-1][l-1]

print(dp)
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])
'''