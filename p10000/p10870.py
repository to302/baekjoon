# coding=utf-8

'''피보나치 수 5
https://www.acmicpc.net/problem/10870
'''

import sys
input = sys.stdin.readline

d = [None for _ in range(21)]
def fib5(n):
    global d
    if n in (0, 1):
        return n

    if (d[n]):
        return d[n]

    val = fib5(n-1) + fib5(n-2)
    d[n] = val
    return val

print(fib5(int(input())))

# pass