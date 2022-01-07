# coding=utf-8

'''대표값2
https://www.acmicpc.net/problem/2587
'''

import sys
input = sys.stdin.readline

arr = []
for _ in range(5):
    arr.append(int(input()))

print(sum(arr)//5)
print(sorted(arr)[2])


# pass


# 수학
# 구현
# 사칙연산