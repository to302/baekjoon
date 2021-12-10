# coding=utf-8

'''고급 수학
https://www.acmicpc.net/problem/7510
'''

import sys
input = sys.stdin.readline

for i in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print('Scenario #{:d}:'.format(i+1))
    if a**2 + b**2 == c**2:
        print('yes')
    else:
        print('no')

    print()

# pass

# 수학
# 기하학
# 피타고라스 정리
