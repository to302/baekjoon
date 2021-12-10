# coding=utf-8

'''컵라면 측정하기
https://www.acmicpc.net/problem/16479
'''

k = int(input())
d1, d2 = map(int, input().split())

h = (k**2 - ((d2 - d1)/2)**2)
print(h)

# pass

# 수학
# 기하학
# 피타고라스 정리
