# coding=utf-8

'''팰린드롬수
https://www.acmicpc.net/problem/1259

어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다. 'radar', 'sees'는 팰린드롬이다.
'''

import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '0':
        break

    if s == s[::-1]:
        print('yes')
    else:
        print('no')

# pass

# 구현
# 문자열
