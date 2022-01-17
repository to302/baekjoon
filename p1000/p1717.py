# coding=utf-8

'''집합의 표현
https://www.acmicpc.net/problem/1717
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ns = [[i, None] for i in range(n+1)] # [parent, child]

def get_root(idx):
    global ns
    while True:
        if ns[idx][0] == idx:
            return(idx)

        idx = ns[idx][0]

def get_leaf(idx):
    global ns
    while True:
        if ns[idx][1] == None:
            return(idx)

        idx = ns[idx][1]


for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0: # 합치기
        if a == b:
            continue

        la = get_leaf(a)
        rb = get_root(b)
        ns[la][1] = rb
        ns[rb][0] = la
        
    elif c == 1: # 출력
        print('YES' if a==b or get_root(a)==get_root(b) else 'NO')

# 시간 초과


# 자료 구조
# 분리 집합    