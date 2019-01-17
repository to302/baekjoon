# coding=utf-8

# https://www.acmicpc.net/problem/1789
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

s = int(input())

n = 1
while(n*(n+1)/2 <= s):
    n += 1

print(n-1)

#pass