# coding=utf-8

# https://www.acmicpc.net/problem/10872
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
# 출력
# 첫째 줄에 N!을 출력한다.

n = int(input())
_t = 1
for i in range(n, 0, -1):
    _t *= i
print(_t)