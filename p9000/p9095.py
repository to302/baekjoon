# coding=utf-8

'''1, 2, 3 더하기
https://www.acmicpc.net/problem/9095

n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력
'''

d = {1:{(1,)}}

def solve(n):
    if n in d.keys():
        return(d[n])

    s = set()
    for i in range(1, n):
        if n-i<=3 and i<=3:
            s.add((n-i, i))

        if n-i > 1:
            ts = solve(n-i)
            for t in ts:
                if i<=3:
                    s.add((t +(i,)))
        elif i > 1:
            ts = solve(i)
            for t in ts:
                if n-i<=3:
                    s.add(((n-i,)+t))
            
    d[n] = s
    return(s)


for _ in range(int(input())):
    n = int(input())
    print(len(solve(n)))


# fail


# 다이나믹 프로그래밍