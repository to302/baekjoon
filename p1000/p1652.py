# coding=utf-8

'''누울 자리를 찾아라
https://www.acmicpc.net/problem/1652
'''

import sys
input = sys.stdin.readline

N = int(input())

arr = []
h = 0 # 가로
v = 0 # 세로
for i in range(N):
    prev_x = True
    a = list(input().rstrip())
    for j in range(N-1):
        if a[j] == 'X':
            prev_x = True
        elif prev_x and a[j] == '.' and a[j+1] == '.':
            h += 1
            prev_x = False
    arr.append(a)

for i in range(N):
    prev_x = True
    for j in range(N-1):
        if arr[j][i] == 'X':
            prev_x = True
        elif prev_x and arr[j][i] == '.' and arr[j+1][i] == '.':
            v += 1
            prev_x = False

print(h, v)   


# pass

# 구현
# 문자열

# a = [''.join(row) for row in zip(*arr)] 행렬 전치



