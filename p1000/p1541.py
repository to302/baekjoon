# coding=utf-8
'''잃어버린 괄호
https://www.acmicpc.net/problem/1541
'''

def fn1():
    import re
    exp = re.compile('[0-9]+')
    exp2 = re.compile('\-|\+')

    s = input().rstrip()

    m = list(map(lambda x: str(int(x)), exp.findall(s)))
    m2 = exp2.findall(s)

    s = ''
    for i in range(len(m)):
        if (i>0 and len(m2)>=i):
            s += m2[i-1]
        s += m[i]

    sc = s.count('-')
    if sc == 0:
        print(eval(s))
    elif sc == 1:
        ns = s.replace('-', '-(') + ')'
        print(eval(ns))
    else:
        ns = '(' + s.replace('-', ')-(') + ')'
        print(eval(ns))


def fn2():
    es = input().rstrip().split('-')
    aa = []
    for e in es:
        ssum = 0
        for i in e.split('+'):
            ssum += int(i)

        aa.append(ssum)
    a = aa[0] - sum(aa[1:])
    print(a)
    


if __name__ == '__main__':
    fn2() # better

# pass    


# 수학
# 문자열
# 그리디 알고리즘
# 파싱

