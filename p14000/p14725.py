# coding=utf-8

'''개미굴
https://www.acmicpc.net/problem/14725
'''

import sys
input = sys.stdin.readline


# d = {'entry':{'a':{'c':1}, 'b':2}}
# dp = d['entry']
# print('a', 'a' in dp.keys())
# dp = dp['a']
# print('c',  'c' in dp.keys())

d = {}
for _ in range(int(input())):
    dp = d
    a = input().rstrip().split()
    for k in a[1:]:
        if k in dp.keys():
            dp = dp[k]
        else:
            dp[k] = {}
            dp = dp[k]

def print_d(d, depth):
    for k in sorted(d.keys()):
        prefix = '--' * depth
        print('{}{}'.format(prefix, k))
        print_d(d[k], depth+1)

print_d(d, 0)

        
# pass

# 문자열
# 자료 구조
# 트리
# 트라이        
    
            
        
        

