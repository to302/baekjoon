# coding=utf-8

'''좌표 압축
https://www.acmicpc.net/problem/18870
'''


import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

dic = dict()
i = 0
for j in sorted(set(arr)):
    dic[j] = i
    i += 1

for i in arr:
    print(dic[i], end=' ')


# pass


# 정렬
# 값 / 좌표 압축