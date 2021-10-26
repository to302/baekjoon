# coding=utf-8

'''스키테일 암호
https://www.acmicpc.net/problem/23080
'''

import sys
input = sys.stdin.readline

K = int(input())
S = input().rstrip()

es = ""
for i in range(0, len(S), K):
    es += S[i]

print(es)

#pass #문자열