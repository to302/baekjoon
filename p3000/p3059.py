# coding=utf-8

'''등장하지 않는 문자의 합
https://www.acmicpc.net/problem/3059
'''

import sys
input = sys.stdin.readline

dic = { chr(v):v for v in range(ord('A'), ord('Z')+1) }

for _ in range(int(input())):
    d = dic.copy()
    for c in input().rstrip():
        d[c] = 0

    print(sum(d.values()))

# pass

# 구현
# 문자열
