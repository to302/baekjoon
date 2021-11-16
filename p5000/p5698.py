# coding=utf-8

'''Tautogram
https://www.acmicpc.net/problem/5698
'''

import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '*':
        break

    if len(set(map(lambda x: x[0].upper(), s.split()))) > 1:
        print('N')
    else:
        print('Y')

# pass    

# 문자열
# 구현
# 파싱
    