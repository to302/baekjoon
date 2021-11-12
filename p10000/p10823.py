# coding=utf-8

'''더하기 2
https://www.acmicpc.net/problem/10823

숫자와 콤마로만 이루어진 문자열 S가 주어진다. 이때, S에 포함되어있는 자연수의 합을 구하는 프로그램을 작성하시오.
S의 첫 문자와 마지막 문자는 항상 숫자이고, 콤마는 연속해서 주어지지 않는다. 주어지는 수는 항상 자연수이다.
'''

import sys

ss = ''
while True:
    s = sys.stdin.readline().rstrip()
    if not s:
        break
    ss += s

print(sum(map(int, ss.split(','))))

# pass

# 수학
# 문자열
# 사칙연산
# 파싱