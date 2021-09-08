# coding=utf-8

'''ACM 호텔
https://www.acmicpc.net/problem/10250
'''

import sys
input = sys.stdin.readline


def assign_room(H, W, N):
    y = (N-1) % H + 1 # 층
    x = (N-1) // H  + 1 # 호
    print("{:d}{:02d}".format(y, x))


T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    assign_room(H, W, N) # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님

#pass

