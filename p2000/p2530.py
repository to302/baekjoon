# coding=utf-8

'''인공지능 시계
https://www.acmicpc.net/problem/2530
'''

H, M, S = map(int, input().split())
D = int(input())

dh, dm, ds = D//3600, (D//60)%60, D%60

om, os = (ds+S)//60, (ds+S)%60
oh, om = (M + dm + om)//60, (M + dm + om)%60
oh = (H + dh + oh)%24

print(oh, om, os)

# pass

# 수학
# 사칙연산
