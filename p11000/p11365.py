# coding=utf-8

'''!밀비 급일
https://www.acmicpc.net/problem/11365
'''

import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == 'END':
        break
    a = [w[::-1] for w in list(reversed(s.split()))]
    print(' '.join(a))

# pass

# 구현
# 문자열