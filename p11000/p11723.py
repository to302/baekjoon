# coding=utf-8

'''집합
https://www.acmicpc.net/problem/11723

1 ≤ x ≤ 20

첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.
'''

# print(int('1'*20))
# print(int('1'*20, base=2))
# print(0b11111111111111111111)


import sys
input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    ss = input().rstrip()
    if ss.startswith(('all','empty')):
        cmd = ss
    else:
        cmd, x = ss.split()
        x = int(x) - 1
    
    if cmd == 'add':
        S = S | (1 << x)
    elif cmd == 'remove':
        S = S & ~(1 << x)
    elif cmd == 'check':
        print(1 if S & (1 << x) else 0)
    elif cmd == 'toggle':
        S = S ^ (1 << x)
    elif cmd == 'all':
        S = int('1'*20, base=2) # (1 << 20) - 1 
    elif cmd == 'empty':
        S = 0

# pass

# 구현
# 비트마스킹
