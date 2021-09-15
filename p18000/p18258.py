    # coding=utf-8

'''큐 2
https://www.acmicpc.net/problem/18258

정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
'''

from collections import deque
import sys
input = sys.stdin.readline

q = deque()

for _ in range(int(input())):
    c = input().rstrip()

    if c[:4] == 'push':
        c, x = c.split()
        x = int(x)

        q.append(x)
    else:
        if c == 'pop':
            print(-1 if len(q) == 0 else q.popleft())
        elif c == 'size':
            print(len(q))
        elif c == 'empty':
            print(1 if len(q)==0 else 0)
        elif c == 'front':
            print(-1 if len(q) == 0 else q[0])
        elif c == 'back':
            print(-1 if len(q) == 0 else q[-1])



#큐 #queue

#pass
