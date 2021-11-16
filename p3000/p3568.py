# coding=utf-8

'''iSharp
https://www.acmicpc.net/problem/3568
'''

def fn1():
    import re
    rex = re.compile(r'([a-zA-Z]+)(\W*)')

    a = input().rstrip(';').split(maxsplit=1)

    for v in a[1].split(','):
        v = v.strip()
        m = rex.match(v)
        print('{}{} {};'.format(a[0], m[2][::-1].replace('][','[]'), m[1]))


def fn2():
    a = input().split(maxsplit=1)
    for v in a[1].rstrip(';').split(','):
        v = v.strip()
        for i in range(len(v)):
            if not v[i].isalpha():
                vn = v[:i]
                t = v[i:][::-1].replace('][','[]')
                break
        else:
            vn = v
            t = ''
        print('{}{} {};'.format(a[0], t, vn))


if __name__ == '__main__':
    fn2() # faster (68ms)
    # fn1() # slower (140ms)



# pass 

# 문자열
# 파싱