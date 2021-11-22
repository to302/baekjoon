# coding=utf-8

'''홀수
https://www.acmicpc.net/problem/2576
'''

mo = 101
sum = 0
for _ in range(7):
    i = int(input())
    if i%2 == 1 :
        sum += i
        mo = min(mo, i)

if mo == 101:
    print(-1)
else:
    print(sum)
    print(mo)

# pass

# 수학
# 구현    