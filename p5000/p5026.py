# coding=utf-8

'''박사 과정
https://www.acmicpc.net/problem/5026
'''

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = input().rstrip()
    if s == 'P=NP':
        print('skipped')
    else:
        print(sum(map(int, s.split('+'))))

# pass

# 구현
# 문자열
# 파싱
