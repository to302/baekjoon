# coding=utf-8

'''동혁 피자
https://www.acmicpc.net/problem/6502
'''

import sys
input = sys.stdin.readline

idx = 0
while True:
    s = input().rstrip()
    if s == '0':
        break
    
    idx += 1
    r, w, l = map(int, s.split())
    if 2*r >= (w**2 + l**2)**0.5:
        print('Pizza {:d} fits on the table.'.format(idx))
    else:
        print('Pizza {:d} does not fit on the table.'.format(idx))

# pass

    
# 수학
# 구현
# 기하학
# 피타고라스 정리
    