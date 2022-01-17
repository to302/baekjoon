# coding=utf-8

'''집합의 표현
https://www.acmicpc.net/problem/1717
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ns = [{i} for i in range(n+1)]
nd = {i:i for i in range(n+1)}

for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        if a == b:
            continue
        
        i1 = nd[a] 
        i2 = nd[b]
        for i in ns[i2]:
            nd[i] = nd[a]
        ns[i1].update(ns[i2])
        ns[i2] = {}

    elif c == 1:
        print('YES' if nd[a] == nd[b] else 'NO')
    
# 메모리 초과

# 자료 구조
# 분리 집합    