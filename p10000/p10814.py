# coding=utf-8

'''나이순 정렬
https://www.acmicpc.net/problem/10814
'''

import sys
input = sys.stdin.readline

dic = dict()
for _ in range(int(input())):
    age, name = input().rstrip().split()
    k = int(age)
    if k in dic.keys():
        dic[k].append(name)
    else:
        dic[k] = [name]
        
for k in sorted(dic.keys()):
    for v in dic[k]:
        print(k, v)


# pass

# 정렬