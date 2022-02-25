# coding=utf-8

'''이상한 곱셈
https://www.acmicpc.net/problem/1225
'''

A, B = input().split()

if len(A) > len(B):
    s = sum(map(int, list(A)))
    arr = B
else:
    s = sum(map(int, list(B)))
    arr = A

print(sum([int(i)*s for i in arr]))


# pass
# 이중 for 로는 시간 초과


# 수학
# 구현
# 문자열

