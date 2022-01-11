# coding=utf-8

'''ATM
https://www.acmicpc.net/problem/11399
'''

N = int(input())
ts = list(map(int, input().split()))
ts.sort()

arr = [0]
for i in range( len(ts)):
    arr.append(arr[i] + ts[i])

print(sum(arr))

# pass

# 그리디 알고리즘
# 정렬