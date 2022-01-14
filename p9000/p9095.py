# coding=utf-8

'''1, 2, 3 더하기
https://www.acmicpc.net/problem/9095

n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
'''

import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    a = [0, 1, 2, 4] + [0] * (n-3)
    for i in range(4, n+1):
        a[i] = a[i-1] + a[i-2] + a[i-3]
    
    print(a[n])

# pass


# 다이나믹 프로그래밍