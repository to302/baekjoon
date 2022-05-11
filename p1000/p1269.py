# coding=utf-8

'''대칭 차집합

https://www.acmicpc.net/problem/1269
'''

an, bn = map(int, input().split())
sa = set(map(int, input().split()))
sb = set(map(int, input().split()))

print (len(sa.difference(sb).union(sb.difference(sa))))

# print(len(sa ^ sb)) # xor의 연산

# pass

