# coding=utf-8

# https://www.acmicpc.net/problem/2407
# nCm을 출력한다.
# 입력
# n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)
# 출력
# nCm을 출력한다.

n, m = map(int, input().split())

_t = 1
for i in range(n, n-m, -1):
    _t *= i

for i in range(m, 0, -1):
    _t /= i

print(int(_t))