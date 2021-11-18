# coding=utf-8

'''16진수
https://www.acmicpc.net/problem/1550

16진수 수를 입력받아서 10진수로 출력하는 프로그램을 작성하시오.
'''

s = input()

len_s = len(s)
out = 0
for i in range(len_s):
    p = 16 ** (len_s - 1 - i)

    if 'A' <= s[i] <= 'F':
        out += p * (10 + ord(s[i]) - ord('A'))
    else:
        out += p * int(s[i])

print(out)

# pass

# 수학
# 구현
