# coding=utf-8

'''벼락치기
https://www.acmicpc.net/problem/23739
'''

import sys
input = sys.stdin.readline

remain = 30
over_half = 0
for _ in range(int(input())):
    i = int(input())
    if remain / i >= 0.5:
        over_half += 1
    
    remain -= i
    if remain <= 0:
        remain = 30
    
print(over_half)

    
# pass

# 수학
# 구현 