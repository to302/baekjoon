# coding=utf-8

'''압축
https://www.acmicpc.net/problem/1662
'''

s = input()
stk = []

for c in s:
    stk.append(c)
    if c == ')':
        t = None
        s = ''
        while t != '(':
            t = stk.pop()
            s = t + s
        r = s.lstrip('(').rstrip(')') * int(stk.pop())
        stk.append(r)
        
print(len(''.join(stk)))

# 메모리 초과

# 자료구조
# 스택
# 재귀
