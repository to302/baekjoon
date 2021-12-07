# coding=utf-8

'''주사위 세개
https://www.acmicpc.net/problem/2480
'''

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    x = a if a == b or a == c else b
    print(1000 + x * 100)
else:
    print(max(a, b, c) * 100)

# pass 


# 수학
# 사칙연산