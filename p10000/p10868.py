# coding=utf-8

'''최솟값
https://www.acmicpc.net/problem/10868
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

for _ in range(M):
    a, b = map(int, input().split())
    print(min(arr[a-1:b]))


# 시간 초과


# 자료 구조
# 세그먼트 트리
# 희소 배열