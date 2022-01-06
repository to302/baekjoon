# coding=utf-8

'''짝수를 찾아라
https://www.acmicpc.net/problem/3058
'''

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ss = sorted(list(filter(lambda x: x%2 == 0, map(int, input().split()))))
    
    print(sum(ss), ss[0])



# pass


# 수학
# 구현
# 사칙연산    