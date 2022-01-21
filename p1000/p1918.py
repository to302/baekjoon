# coding=utf-8

'''후위 표기식
https://www.acmicpc.net/problem/1918
'''

# s = list(input())
# s = list('A+B*C-D/E') # ABC*+DE/-
s = list('A+B*C') # ABC*+
# s = list('A*(B+C)') # ABC+*

op = {'+':1, '-':1, '*':3, '/':3, '(':2, ')':2}

stk = []
for c in s:
    if c not in op.keys():
        print(c, end='')
    else:
        if len(stk) > 0 :
            e = stk[-1]
            if op[c] < op[e]:
                for o in reversed(stk):
                    print(o, end='')
                stk.clear()
        
        stk.append(c)    

for o in reversed(stk):
    print(o, end='')
