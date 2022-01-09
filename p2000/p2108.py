# coding=utf-8

'''통계학
https://www.acmicpc.net/problem/2108

첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
'''

import sys
input = sys.stdin.readline


N = int(input())
dic = dict()
for _ in range(N):
    i = int(input())
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

items = dic.items()


# 산술평균
print(round(sum([k*v for k, v in items]) / N))
    
# 중앙값
m = (N//2) + 1
acc = 0
for k, v in sorted(items):
    acc += v
    if acc >= m:
        print(k)
        break

# 최빈값
a = sorted(items, key=lambda x: (x[1],-x[0]), reverse=True)
print(a[0][0] if (len(a)==1 or a[0][1] > a[1][1]) else a[1][0])

# 범위
a = max(items, key=lambda x:x[0]) 
b = min(items, key=lambda x:x[0])
print(a[0] - b[0])


# pass -> from collections import Counter 을 이용하는 방법도 있음.(내 방식이 빠르긴 함)
# statistics 모듈 이용하는 방법  multimode (3.8 에 추가됨)


# 구현
# 정렬
