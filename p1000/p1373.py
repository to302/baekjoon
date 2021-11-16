# coding=utf-8

'''2진수 8진수
https://www.acmicpc.net/problem/1373
'''

def fn1():
    s = input().rstrip()

    d = {
        '000':'0',
        '001':'1',
        '010':'2',
        '011':'3',
        '100':'4',
        '101':'5',
        '110':'6',
        '111':'7'
    }

    r = ''
    for i in range(len(s), -1, -3):
        u = s[max(0,i-3):i]
        u = '0'*(3-len(u)) + u
        r = d[u] + r

    while r[0] == '0' and len(r)>1:
        r = r[1:]

    print(r)


def fn2():
    s = input().rstrip()

    d = {
        '000':'0',
        '001':'1',
        '010':'2',
        '011':'3',
        '100':'4',
        '101':'5',
        '110':'6',
        '111':'7'
    }

    m3 = len(s) % 3
    if m3 > 0:
        s = '0' * (3 - m3) + s
    
    r = ''
    for i in range(0, len(s), 3):
        k = s[i:i+3]
        r += d[k]
    
    print(r)

if __name__ == '__main__':
    fn2() # faster 160ms
    # fn1() # slower 3856ms


# pass 

# 수학
# 문자열
