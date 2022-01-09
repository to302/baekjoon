# coding=utf-8

'''좌표 정렬하기 2
https://www.acmicpc.net/problem/11651

2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    arr.append((x,y))

arr.sort(key=lambda x:(x[1],x[0]))
for x, y in arr:
    print(x, y)

# pass

# 정렬
