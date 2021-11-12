# coding=utf-8

'''8진수, 10진수, 16진수
https://www.acmicpc.net/problem/11816

정수 X가 주어진다. 정수 X는 항상 8진수, 10진수, 16진수 중에 하나이다.
8진수인 경우에는 수의 앞에 0이 주어지고, 16진수인 경우에는 0x가 주어진다.
X를 10진수로 바꿔서 출력하는 프로그램을 작성하시오.
'''

s = input().rstrip()

HNUM = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

def hex_to_dec(x):
    v = 0
    len_x = len(x)
    for i in range(len_x):
        if x[i] in HNUM.keys():
            xi = HNUM[x[i]]
        else:
            xi = int(x[i])

        v += xi * (16**(len_x-i-1)) 

    return(v)
   

def oct_to_dec(x):
    v = 0
    len_x = len(x)
    for i in range(len_x):
        v += int(x[i]) * (8**(len_x-i-1)) 

    return(v)

if s.startswith('0x'):
    print(hex_to_dec(s[2:]))
elif s.startswith('0'):
    print(oct_to_dec(s[1:]))
else:
    print(int(s))

# pass

# 수학
# 구현
# 문자열
# 사칙연산
# 파싱
