# coding=utf-8

'''오븐 시계
https://www.acmicpc.net/problem/2525
'''

h, m = map(int, input().split())
dm = int(input())

u = (m+dm)//60
m = (m+dm)%60
h += u
if h >= 24:
    h -= 24

print('{} {}'.format(h, m))

# pass

# 수학
# 사칙연산
