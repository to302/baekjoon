# coding=utf-8

'''가장 많은 글자
https://www.acmicpc.net/problem/1371
'''

import sys

ss = ''
for _ in range(50):
    s = sys.stdin.readline()
    ss += s

max_cnt = 0
max_chr = []
for i in range(ord('a'), ord('z')+1):
    c = chr(i)
    c_cnt = ss.count(c)

    if c_cnt == max_cnt :
        max_chr.append(c)
    elif c_cnt > max_cnt:
        max_chr.clear()
        max_chr.append(c)
        max_cnt = c_cnt
    else:
        pass

print("".join(sorted(max_chr)))

# pass

# 구현
# 문자열
