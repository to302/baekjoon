# coding=utf-8

'''소수 단어
https://www.acmicpc.net/problem/2153
'''

la = ord('a')
lz = ord('z')
ua = ord('A')
uz = ord('Z')

sum = 0
for w in input().rstrip():
    wi = ord(w)
    if wi <= uz:
        sum += wi - ua + 1
    else:
        sum += wi - la + 1

is_prime = True
for i in range(2, int(sum**0.5)+1):
    if sum % i == 0 :
        is_prime = False
        break
    
if is_prime:    
    print('It is a prime word.')
else:
    print('It is not a prime word.')

# pass

# 수학
# 문자열
# 정수론
# 소수 판정