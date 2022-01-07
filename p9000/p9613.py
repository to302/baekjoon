# coding=utf-8

'''GCD 합
https://www.acmicpc.net/problem/9613
'''

import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(map(int, input().split()))[1:]
    ans = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            ans += math.gcd(arr[i], arr[j]) 
            
    print(ans)

# pass

# 수학
# 정수론
# 유클리드 호제법