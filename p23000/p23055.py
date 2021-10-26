# coding=utf-8

'''공사장 표지판
https://www.acmicpc.net/problem/23055
'''

N = int(input())

for i in range(N):
    if i in (0, N-1):
        print('*' * N)
    else:
        t = [' ' for _ in range(N)]
        t[0] = '*'
        t[N-1] = '*'
        t[i] = '*'
        t[N-1-i] = '*'
        print(''.join(t))

#pass