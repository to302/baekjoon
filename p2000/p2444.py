# coding=utf-8

'''별 찍기 - 7
https://www.acmicpc.net/problem/2444
'''

T = int(input())
maxW = T * 2 - 1

for i in range(1, T):
    s = "*" * (i*2 - 1)
    print(s.center(maxW).rstrip())
    

for i in range(T, 0, -1):
    s = "*" * (i*2 - 1)
    print(s.center(maxW).rstrip())

# pass

# 구현
