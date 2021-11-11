# coding=utf-8

'''큰 수 A+B
https://www.acmicpc.net/problem/10757
파이썬 같은 언어는 10,000자리 정도의 자연수도 자유롭게 다룰 수 있습니다. 
하지만 C/C++이라면 이 문제를 어떻게 풀까요? C/C++ 사용자가 아니더라도 고민해 보면 좋을 것입니다.

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A,B < 10**10000)

출력
첫째 줄에 A+B를 출력한다.
'''

def zeropadding(x, n):
    return ('0'*(n - len(x)) + x)

A, B = input().split()

lenA = len(A)
lenB = len(B)
mlen = max(lenA, lenB)

A = zeropadding(A, mlen)
B = zeropadding(B, mlen)

ans = []
lift = 0
for i in range(mlen, 0, -4):
    s = max(0, i-4)
    aa, bb = map(int, (A[s:i], B[s:i]))
    ab = str(aa + bb + lift)
    lift = 0

    if s == 0:
        ans.append(zeropadding(ab, 4))
    else:
        if len(ab)>4:
            lift = int(ab[:-4])
            ab = ab[-4:]
        ans.append(zeropadding(ab, 4))

print(int(''.join(reversed(ans))))


# pass

# 수학
# 구현
# 사칙연산
# 임의 정밀도 / 큰 수 연산