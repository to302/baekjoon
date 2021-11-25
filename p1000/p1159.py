# coding=utf-8

'''농구 경기
https://www.acmicpc.net/problem/1159
'''

import sys
input = sys.stdin.readline

d = dict()
for _ in range(int(input())):
    c = input()[0]
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1

out = sorted(filter(lambda x: x[1]>=5, d.items()))
if len(out) == 0:
    print('PREDAJA')
else:
    print(''.join([i for i,j in out]))

# pass

# 문자열
