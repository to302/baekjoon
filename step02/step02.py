# -*- coding: utf-8 -*-

# # 문제 : https://www.acmicpc.net/problem/10998
# a, b = map(int, input().split())
# print(a*b)

# # 문제 : https://www.acmicpc.net/problem/1008
# a, b = map(int, input().split())
# print(a/b)

# # 문제 : https://www.acmicpc.net/problem/10869
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(int(a/b))
# print(a%b)

# # 문제 : https://www.acmicpc.net/problem/10430
# a, b, c = map(int, input().split())
# print((a+b)%c)
# print((a%c + b%c)%c)
# print((a*b)%c)
# print((a%c * b%c)%c)

# # 문제 : https://www.acmicpc.net/problem/2558
# a = int(input())
# b = int(input())
# print(a+b)

# 문제 : https://www.acmicpc.net/problem/2839
n = int(input())
max_5 = int(n/5)
div_5 = n%5

for i in range(max_5, -1, -1):    
    if (div_5 % 3 == 0):
        print(i + int(div_5/3))
        break

    div_5 += 5
else:
    print(-1)    