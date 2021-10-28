# coding=utf-8

'''A와 B
https://www.acmicpc.net/problem/12904
'''

S = input().rstrip()
T = input().rstrip()

while len(T)>len(S):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]

print(1 if S == T else 0)


# pass

# 구현
# 문자열
# 그리디 알고리즘
