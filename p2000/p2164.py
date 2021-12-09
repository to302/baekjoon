# coding=utf-8

'''카드2
https://www.acmicpc.net/problem/2164
'''

from collections import deque

N = int(input()) # 1 <= N <= 50,0000
que = deque([i for i in range(1, N+1)])

def fn1():
    idx = 0
    while len(que) > 1:
        if idx % 2 == 0:
            que.popleft()
        else:
            que.append(que.popleft())

        idx += 1

    print(que.popleft())


def fn2():
    while len(que) > 1:
        que.popleft()
        que.append(que.popleft())

    print(que.popleft())



if __name__ == '__main__':
    fn1()
    fn2() # faster


# pass - fn1, fn2

# 자료구조
# 큐