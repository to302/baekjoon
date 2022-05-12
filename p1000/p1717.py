# coding=utf-8

'''집합의 표현
https://www.acmicpc.net/problem/1717
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def get_root(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = get_root(parent[x])
        return parent[x] 
    
def union_root(x, y):
    xr = get_root(x)
    yr = get_root(y)

    if xr != yr:
        parent[xr] = yr
    

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_root(a, b)
    elif op == 1:
        if get_root(a) == get_root(b):
            print('YES')
        else:
            print('NO')
        

# pass

# 자료 구조
# 분리 집합 (Disjoint Set)
#   
# 참고 : https://4legs-study.tistory.com/94