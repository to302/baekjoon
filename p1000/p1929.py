# coding=utf-8

'''소수 구하기
https://www.acmicpc.net/problem/1929

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
'''

## Sieve of Eratosthenes 
M, N = map(int, input().split())

sieve = [True] * (N+1)
sieve[0:1] = False, False

for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(i+i, N+1, i):
            sieve[j] = False

for i in range(M, N+1):
    if sieve[i]:
        print(i)

#pass