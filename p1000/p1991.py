# coding=utf-8

'''트리 순회
https://www.acmicpc.net/problem/1991
'''

def preorder(n):
    global d
    if n == '.':
        return('')
    return(n + preorder(d[n][0]) + preorder(d[n][1]))

def inorder(n):
    global d
    if n == '.':
        return('')
    return ( inorder(d[n][0]) + n + inorder(d[n][1]))

def postorder(n):
    global d
    if n == '.':
        return('')
    return ( postorder(d[n][0]) + postorder(d[n][1]) + n )

d = dict()
for _ in range(int(input())):
    p, l, r = input().split()
    d[p] = (l, r)

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))

# pass

# 트리
# 재귀