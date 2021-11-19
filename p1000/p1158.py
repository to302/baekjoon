# coding=utf-8

'''요세푸스 문제
https://www.acmicpc.net/problem/1158
'''

n, k = map(int, input().split())
q = [str(i) for i in range(1, n+1)]

out = []
i = k - 1
while len(q) > 0:
    if i >= len(q):
        i %= len(q)
    
    out.append(q.pop(i))
    
    i += (k - 1)

print('<{}>'.format(', '.join(out)))

# pass


# 자료구조
# 큐
