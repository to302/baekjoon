# coding=utf-8

'''배수와 약수
https://www.acmicpc.net/problem/5086
'''

import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    
    if a>b:
        if a % b == 0:
            print('multiple')
        else:
            print('neither')
    elif a<b:
        if b % a == 0:
            print('factor')
        else:
            print('neither')
        
# pass
        

# 수학
# 구현
# 사칙연산