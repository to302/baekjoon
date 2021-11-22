# coding=utf-8

'''별 찍기 - 9
https://www.acmicpc.net/problem/2446
'''

N = int(input())
mi = 2*N-1
for i in range(N, 1, -1):
    ti = 2*i-1
    mg = (mi - ti)//2
    print(' '*mg + '*' * ti)

for i in range(1, N+1):
    ti = 2*i-1
    mg = (mi - ti)//2
    print(' '*mg + '*' * ti)

# pass

# 구현