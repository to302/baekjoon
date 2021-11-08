# coding=utf-8

'''학점계산
https://www.acmicpc.net/problem/2754
'''

# g = 0
# for c in ('A','B','C','D'):
#     g2 = 0.3
#     for m in ('+','0','-'):
#         print("'{}':{}".format(c+m, 4-g+g2), end=', ')
#         g2 -= 0.3
#     g += 1

d = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}

print(d[input().rstrip()])

# 문자열

# pass