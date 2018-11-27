# coding=utf-8

# https://www.acmicpc.net/problem/2261
# 2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 자연수 n(2 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 차례로 각 점의 x, y좌표가 주어진다. 
# 각각의 좌표는 절댓값이 10,000을 넘지 않는 정수이다. 같은 점이 여러 번 주어질 수도 있다.
# 출력
# 첫째 줄에 가장 가까운 두 점의 거리의 제곱을 출력한다.

import sys
input = sys.stdin.readline

dist = lambda xy1,xy2: (xy1[0]-xy2[0])**2 + (xy1[1]-xy2[1])**2   

n = int(input())
dl = []
min = None
for i in range(n):
    print(set(input().split()))
    #dl.append(list(map(int, input().split())))
    
#print(dl)

