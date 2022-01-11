# coding=utf-8

'''럭키 스트레이트
https://www.acmicpc.net/problem/18406
'''

N = input()
len_n = len(N)//2
a = sum(map(int, N[:len_n]))
b = sum(map(int, N[len_n:]))
print('LUCKY' if a==b else 'READY')

# pass

# 구현
# 문자열