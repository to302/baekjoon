# coding=utf-8

'''신나는 함수 실행
https://www.acmicpc.net/problem/9184
'''

import sys
input = sys.stdin.readline

v = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]
def w(a, b, c):
    global v
   
    if (a <= 0 or b <= 0 or c <= 0 ):
        return 1
    elif (a > 20 or b > 20 or c>20):
        return w(20, 20, 20)

    if (v[a][b][c]):
        return v[a][b][c]

    if (a < b < c):
        val = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        val = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    v[a][b][c] = val
    return(val)

while True:
    a, b, c = map(int, input().split())
    if (a==-1 and b==-1 and c==-1):
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))


# pass    