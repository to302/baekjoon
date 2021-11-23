# coding=utf-8

'''베스트셀러
https://www.acmicpc.net/problem/1302
'''

import sys
input = sys.stdin.readline

d = dict()
for _ in range(int(input())):
    k = input().rstrip()
    if k in d.keys():
        d[k] += 1
    else:
        d[k] = 1

mval = max(d.values())
a = list(filter(lambda x:x[1]==mval, d.items()))
print(sorted(a)[0][0])

# pass

# 자료구조
# 문자열
# 정렬
# 해시를 사용한 집합과 맵
