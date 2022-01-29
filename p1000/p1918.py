# coding=utf-8

'''후위 표기식
https://www.acmicpc.net/problem/1918
'''

# 
# s = list('A+B*C-D/E') # ABC*+DE/-
# s = list('A+B*C') # ABC*+
# s = list('A*(B+C)') # ABC+*
#s = list('((A+B)*(C-D))/E') # AB+CD-*E/

s = list(input())

ops = {'+':1, '-':1, '*':2, '/':2, '(':0 }  
stk = []

for c in s:
    if c == '(':
        stk.append(c)
    elif c == ')':
        while True:
            op = stk.pop()
            if op == '(':
                break
            print(op, end='')
    elif c in ops.keys():
        if len(stk) == 0:
            stk.append(c)
        else:
            while True:
                if len(stk) == 0:
                    break

                if ops[c] <= ops[stk[-1]]:
                    print(stk.pop(), end='')
                else:
                    break
            stk.append(c)
    else:
        print(c, end='')
    
for op in reversed(stk):
    print(op, end='')



# pass 

# 자료 구조
# 스택    