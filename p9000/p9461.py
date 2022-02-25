# coding=utf-8

'''파도반 수열 Padovan sequence
https://www.acmicpc.net/problem/9461
'''

import sys
input = sys.stdin.readline

plist = [0,1,1,1,2,2,3,4,5,7,9]

def solve(N: int) -> int:
    global plist
    if len(plist) > N:
        return plist[N]
    
    for i in range(len(plist), N+1):
        v = plist[i-1] + plist[i-5]
        plist.append(v)

    return plist[N]


for _ in range(int(input())):
    print( solve(int(input())) )

# pass

# 수학
# 다이나믹 프로그래밍