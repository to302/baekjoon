# coding=utf-8

'''균형잡힌 세상
https://www.acmicpc.net/problem/4949

하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.
입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
'''

import sys
input = sys.stdin.readline

while True:
    str = input().rstrip() 
    if str == ".":
        break
    
    s = []
    for c in str:
        if c in ['[','(']:
            s.append(c)
        elif c in [')',']']:
            if len(s) > 0:
                if (c==')' and s[-1]=='(') or (c==']' and s[-1]=='['):
                    s.pop()
                else:
                    s.append(c)
            else:
                print("no")
                break
    else:
        if len(s) == 0:
            print('yes')    
        else:
            print('no')
        
#stack

#pass