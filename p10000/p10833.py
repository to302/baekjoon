# coding=utf-8

import sys
input = sys.stdin.readline

N = int(input())
rsum = 0
for _ in range(N):
    ns, na = map(int, input().split())
    rsum += (na % ns)

print(rsum)

# pass

# 수학
# 사칙연산
