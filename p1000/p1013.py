# coding=utf-8

'''Contact
https://www.acmicpc.net/problem/1013

골드5
'''

import re
import sys
input = sys.stdin.readline

pattern = re.compile('(100+1+|01)+')

def match_pattern(s):
    if pattern.fullmatch(s) == None:
        print('NO')
    else:
        print('YES')

for _ in range(int(input())):
    s = input().rstrip()
    match_pattern(s)

# pass





#문자열
#정규 표현식