# coding=utf-8

'''버그왕
https://www.acmicpc.net/problem/3447
'''

import sys
input = sys.stdin.readline

while True:
    s = input()
    if not s:
        break
    s = s.rstrip()

    while True:
        idx = s.find('BUG')
        if idx == -1:
            break
        s = s.replace('BUG','')
    
    print(s)

# pass
# 
# 문자열
# 파싱    