# coding=utf-8

'''N번째 큰 수
https://www.acmicpc.net/problem/2075
'''

import heapq
import sys
input = sys.stdin.readline

N = int(input())
minh = [*map(int, input().split())]

for _ in range(N-1):
    arr = list(map(int, input().split()))

    for i in arr:
        if i > minh[0]:
            heapq.heappush(minh, i)
            heapq.heappop(minh)

print(minh[0])


# pass


# 자료 구조
# 정렬
# 우선순위 큐
