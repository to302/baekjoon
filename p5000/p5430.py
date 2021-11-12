# coding=utf-8

'''AC
https://www.acmicpc.net/problem/5430

두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 
배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
'''

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip() # 함수
    n = int(input()) # 배열 내의 수의 개수
    arr = deque(input().strip()[1:-1].split(',')) # 배열 (268ms)
    if n == 0:
        arr = deque()
    PT = 'H'

    for c in p:
        if c == 'R':
            PT = 'T' if PT == 'H' else 'H'
        elif c == 'D':
            if len(arr) == 0:
                print('error')
                break
            if PT == 'H':
                arr.popleft()
            else:
                arr.pop()
    else:
        r = '[' + ','.join(arr if PT == 'H' else reversed(arr)) + ']'
        print(r)

# pass 
# deque 를 사용해서 실제 reverse 를 행하지 않고 처리   




# 구현
# 자료 구조
# 문자열
# 파싱
# 덱