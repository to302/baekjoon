# coding=utf-8

'''수 정렬하기 2
https://www.acmicpc.net/problem/2751
'''

import sys

a = set()
for _ in range(int(input())):
    a.add(int(sys.stdin.readline()))

for i in sorted(a):
    print(i)


# pass

# 정렬