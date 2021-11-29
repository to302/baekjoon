# coding=utf-8

'''가운데를 말해요
https://www.acmicpc.net/problem/1655
'''

import heapq
import sys
input = sys.stdin.readline

maxh = []
minh = []
for _ in range(int(input())):
    val = int(input())

    if not maxh and not minh:
        heapq.heappush(maxh, -val)
        print(val)
    elif maxh:
        if val >= -maxh[0]:
            heapq.heappush(minh, val)
        else:
            heapq.heappush(maxh, -val)

        if len(maxh) == len(minh):
            print(min(-maxh[0], minh[0]))
        elif len(maxh) == len(minh)+1:
            print(-maxh[0])
        elif len(maxh)+1 == len(minh):
            print(minh[0])
        elif len(maxh)+2 == len(minh):
            heapq.heappush(maxh, -heapq.heappop(minh))
            print(min(-maxh[0], minh[0]))
        elif len(maxh) == len(minh)+2:
            heapq.heappush(minh, -heapq.heappop(maxh))
            print(min(-maxh[0], minh[0]))

# pass

# 자료구조
# 우선순위 큐
