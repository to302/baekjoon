# coding=utf-8

'''이진수 연산
https://www.acmicpc.net/problem/12813
'''

A = input()
B = input()

len_A = len(A)

l_and = ['0'] * len_A
l_or = ['0'] * len_A
l_xor = ['0'] * len_A
l_not_a = ['0'] * len_A
l_not_b = ['0'] * len_A

for i in range(len_A):
    if A[i] == '0' and B[i] == '0':
        # l_and[i] = '0'
        # l_or[i] = '0'
        # l_xor[i] = '0'
        l_not_a[i] = '1'
        l_not_b[i] = '1'
    elif A[i] == '0' and B[i] == '1':
        # l_and[i] = '0'
        l_or[i] = '1'
        l_xor[i] = '1'
        l_not_a[i] = '1'
        # l_not_b[i] = '0'
    elif A[i] == '1' and B[i] == '0':
        # l_and[i] = '0'
        l_or[i] = '1'
        l_xor[i] = '1'
        # l_not_a[i] = '0'
        l_not_b[i] = '1'
    elif A[i] == '1' and B[i] == '1':
        l_and[i] = '1'
        l_or[i] = '1'
        # l_xor[i] = '0'
        # l_not_a[i] = '0'
        # l_not_b[i] = '0'

print(''.join(l_and))
print(''.join(l_or))
print(''.join(l_xor))
print(''.join(l_not_a))
print(''.join(l_not_b))


def fn2():
    a = int(input(),2)
    b = int(input(),2)
    print(f'{a&b:0100000b}')
    print(f'{a|b:0100000b}')
    print(f'{a^b:0100000b}')
    print(f'{~a & (1<<100000)-1:0100000b}')
    print(f'{~b & (1<<100000)-1:0100000b}')


def fn3():
    a,b=int(input(),2),int(input(),2)
    n=100000
    m=2**n-1
    print(*[bin(N)[2:].zfill(n) for N in [a&b,a|b,a^b,a^m,b^m]],sep='\n')


# pass

# 문자열