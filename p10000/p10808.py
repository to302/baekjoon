# coding=utf-8

'''알파벳 개수
https://www.acmicpc.net/problem/10808
'''

S = input().strip()
d = dict()
for i in range(ord('a'), ord('z')+1):
    d[chr(i)] = 0

for c in S:
    d[c] += 1

for i in range(ord('a'), ord('z')+1):
    print(d[chr(i)], end=' ')

print()
    
#pass #문자열 #구현 