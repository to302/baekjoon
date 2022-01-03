# coding=utf-8

'''구간 합 구하기 4
https://www.acmicpc.net/problem/11659
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ns = list(map(int, input().rstrip().split()))

acc = [0, ns[0]]
for i in range(1, len(ns)):
    acc.append(acc[-1]+ns[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(acc[j] - acc[i-1])


# pass

# 누적 합

