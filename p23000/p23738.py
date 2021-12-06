# coding=utf-8

'''Ресторан
https://www.acmicpc.net/problem/23738
'''

cmap = {'B':'v', 'E':'ye', 'H':'n', 'P':'r', 'C':'s', 'Y':'u', 'X':'h'}

s = input()
out = ''
for c in s:
    if c in cmap.keys():
        out += cmap[c]
    else:
        out += c.lower()

print(out)

# pass

# 구현
# 문자열