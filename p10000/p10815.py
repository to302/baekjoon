# coding=utf-8

'''숫자 카드

https://www.acmicpc.net/problem/10815
'''

N = int(input())
ns = set(map(int, input().split()))
M = int(input())
ms = list(map(int, input().split()))

for i in ms:
    if i in ns:
        print(1, end = ' ')
    else:
        print(0, end=' ')

# pass

# 정렬
# 이분탐색