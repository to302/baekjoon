# coding=utf-8

# https://www.acmicpc.net/problem/2740
# N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 행렬 A의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 순서대로 주어진다. 
# 그 다음 줄에는 행렬 B의 크기 M과 K가 주어진다. 이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다. 
# N과 M, 그리고 K는 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
# 출력
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

# import numpy as np

from sys import stdin

ml = []
for _ in range(2):
    r, c = map(int, stdin.readline().rstrip().split())
    _m1 = []
    for i in range(r):
        _m1.append(list(map(int, stdin.readline().rstrip().split())))
    ml.append(_m1)

n = len(ml[0])
m = len(ml[0][0])
k = len(ml[1][0])

r = [[None]*k for _ in range(n)]

for _n in range(n):
    for _k in range(k):
        _tt = 0
        for _m in range(m):
            _tt += ml[0][_n][_m] * ml[1][_m][_k]
        r[_n][_k] = _tt

for i in r:
    for j in i:
        print(j, end=" ")
    print("")

# print(np.array(ml[0]).dot(np.array(ml[1])))