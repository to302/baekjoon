# coding=utf-8

'''경고
https://www.acmicpc.net/problem/3029

브론즈3
'''

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

if s1 > s2:
    s = 60 + s2 - s1
    m2 -= 1
else:
    s = s2 - s1

if m1 > m2:
    m = 60 + m2 - m1
    h2 -= 1
else:
    m = m2 - m1

if h1 > h2:
    h = 24 + h2 - h1
else:
    h = h2 - h1

if h + m + s == 0:
    h = 24

print("{:02d}:{:02d}:{:02d}".format(h, m, s))

# pass

#수학
#구현
#문자열
#사칙연산
    



