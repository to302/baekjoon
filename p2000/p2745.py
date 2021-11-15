# coding=utf-8

'''진법 변환
https://www.acmicpc.net/problem/2745
'''

N, B = input().split()

B = int(B)
m = len(N) - 1
out = 0
for c in N:
    if 'A' <= c <= 'Z':
        i = ord(c) - ord('A') + 10
    else:
        i = int(c)

    out += (B ** m) * i
    m -= 1

print(out)

# pass

# 수학
# 구현
# 문자열

