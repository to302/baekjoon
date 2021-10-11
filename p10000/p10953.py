# coding=utf-8
'''A+B - 6
https://www.acmicpc.net/problem/10953
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().strip().split(','))
    print(A+B)


#pass #수학 #문자열 #사칙연산 #파싱 