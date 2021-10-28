# coding=utf-8

'''단어 뒤집기
https://www.acmicpc.net/problem/9093
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    words = input().rstrip().split()
    t_ = list(map(lambda x: x[::-1], words))
    print(' '.join(t_))

# pass

# 구현
# 문자열
