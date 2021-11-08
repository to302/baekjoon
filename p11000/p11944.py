# coding=utf-8

'''NN
https://www.acmicpc.net/problem/11944
'''

N, M = map(int, input().split())

nc = str(N) * N
print(nc if len(nc) <= M else nc[:M])

# pass

# 문자열
