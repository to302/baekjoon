# coding=utf-8

'''그릇
https://www.acmicpc.net/problem/7567
'''

s = input()

prev = ''
h = 0 
for c in s:
    h += (5 if prev == c else 10)
    
    prev = c
         
print(h)

# pass

# 구현
# 문자열
