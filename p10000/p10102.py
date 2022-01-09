# coding=utf-8

'''개표
https://www.acmicpc.net/problem/10102

A와 B가 한 오디션 프로의 결승전에 진출했다. 결승전의 승자는 심사위원의 투표로 결정된다.
심사위원의 투표 결과가 주어졌을 때, 어떤 사람이 우승하는지 구하는 프로그램을 작성하시오.

입력
입력은 총 두 줄로 이루어져 있다. 첫째 줄에는 심사위원의 수 V (1 ≤  V ≤  15)가 주어지고, 둘째 줄에는 각 심사위원이 누구에게 투표했는지가 주어진다. A와 B는 각각 그 참가자를 나타낸다.

출력
    A가 받은 표가 B보다 많은 경우에는 A
    B가 받은 표가 A보다 많은 경우에는 B
    같은 경우에는 Tie
를 출력한다.
'''

import sys
input = sys.stdin.readline

V = int(input())
s = input().rstrip()
a = s.count('A') 
b = s.count('B')

if a == b:
    print('Tie')
elif a > b:
    print('A')
else: 
    print('B')

# pass

# 문자열    
