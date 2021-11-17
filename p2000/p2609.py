# coding=utf-8

'''최대공약수와 최소공배수
https://www.acmicpc.net/problem/2609

최대공약수, 최소공배수 구하기 (24, 18) => (6, 72)
'''

n1, n2 = sorted(map(int, input().split()))
a, b = n1, n2

while True:
    r = b % a 
    if r == 0:
        gcd = a
        break
    else:
        b = a
        a = r

lcm = int(n2 * (n1/gcd))

print(gcd) # Greatest Common Divisor
print(lcm) # Least Common Multiple


# pass

# 수학
# 정수론
# 유클리드 호제법
