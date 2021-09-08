# coding=utf-8

'''손익분기점
https://www.acmicpc.net/problem/1712
'''

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split()) # 고정비, 변동비, 가격

if B >= C:
    print(-1)
else:
    print(A//(C-B) + 1) # // 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함

# pass
