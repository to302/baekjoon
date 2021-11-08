# coding=utf-8

'''대소문자 바꾸기
https://www.acmicpc.net/problem/2744
'''




s = input().rstrip()

# print(s.swapcase()) # 관련 기능 함수

la = ord('a')
ua = ord('A')
for c in s:
    si = ord(c)
    if (si >= la):
        print(chr(ua + (si - la)), end='')
    else:
        print(chr(la + (si - ua)), end='')


# pass

# 구현
# 문자열
