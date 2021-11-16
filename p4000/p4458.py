# coding=utf-8

'''첫 글자를 대문자로
https://www.acmicpc.net/problem/4458

문장을 읽은 뒤, 줄의 첫 글자를 대문자로 바꾸는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input()
    print('{}{}'.format(s[0].upper(), s[1:]), end='')
    
# pass

# 문자열
# 구현

