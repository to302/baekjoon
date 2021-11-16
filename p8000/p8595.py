# coding=utf-8

'''히든 넘버 
https://www.acmicpc.net/problem/8595
'''

def fn1():
    '''slower'''
    _ = input()
    s = input()

    out = []
    t = ''
    for c in s:
        if '0'<= c <= '9':
            t += c
        else:
            if t != '':
                out.append(int(t))
                t = ''

    if t != '':
        out.append(int(t))

    print(sum(out))

def fn2():
    '''faster'''
    import re 

    _ = input()
    s = input()
    
    rex = re.compile('[a-zA-Z]+')
    
    print(sum(map(int , filter(lambda x: x !='', rex.split(s)))))
    
if __name__ == '__main__':
    fn2() # faster
    # fn1() # slower

# pass

# 문자열
# 파싱
