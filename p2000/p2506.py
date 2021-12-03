# coding=utf-8

'''점수계산
https://www.acmicpc.net/problem/2506
'''

N = int(input())
G = map(int, input().split())

pt = 0
acc = 0
for i in G:
    if i == 0:
        acc = 0
    elif i == 1:
        acc += i
        pt += acc

print(pt)


# 수학
# 구현
# 사칙연산