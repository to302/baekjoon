# coding=utf-8

'''문자열 분석
https://www.acmicpc.net/problem/10820
'''

import sys

while True:
    s = sys.stdin.readline()
    if not s:
        break
    
    l, u, n, b = 0, 0, 0, 0
    for c in s:
        if 'a' <= c <= 'z':
            l += 1
        elif 'A' <= c <= 'Z':
            u += 1
        elif '0' <= c <='9':
            n += 1
        elif c == ' ':
            b += 1

    print(l, u, n, b)

# pass

# 구현
# 문자열
