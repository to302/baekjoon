# coding=utf-8

# https://www.acmicpc.net/problem/10817
# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 
# 입력
# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
# 출력
# 두 번째로 큰 정수를 출력한다.

import sys
l = list(map(int, sys.stdin.readline().rstrip().split()))
l.sort()
print(l[1])