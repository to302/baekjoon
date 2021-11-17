# coding=utf-8

'''보물
https://www.acmicpc.net/problem/1026
'''

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)

out = 0
for i in range(N):
    out += A[i] * B[i]

print(out)

# pass

# 수학
# 그리디 알고리즘
# 정렬