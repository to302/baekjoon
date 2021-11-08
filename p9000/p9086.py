# coding=utf-8

'''문자열
https://www.acmicpc.net/problem/9086
'''

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    print('{}{}'.format(s[0],s[-1]))

# pass

# 구현
# 문자열
    