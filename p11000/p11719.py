# coding=utf-8

'''그대로 출력하기 2
https://www.acmicpc.net/problem/11719
'''

def fn1():
    import sys
    print(sys.stdin.read())

def fn2():
    while True:
        try:
            s = input()
            print(s)
        except EOFError:
            break

if __name__ == '__main__':
    fn1() # faster
    # fn2()        