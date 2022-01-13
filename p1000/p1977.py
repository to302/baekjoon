# coding=utf-8

'''완전제곱수
https://www.acmicpc.net/problem/1977
'''

M = int(input())
N = int(input())

sm = int(M ** 0.5) 
sn = int(N ** 0.5) + 1

arr = []
for i in range(sm, sn):
    if M <= (i ** 2) <= N:
        arr.append(i**2)
    
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
        
# pass


# 수학
# 구현