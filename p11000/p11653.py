# coding=utf-8

'''소인수분해
https://www.acmicpc.net/problem/11653

정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
'''

N = int(input())

p = []
while True:
    for i in range(2, int(N**0.5) + 2):
        if N % i == 0 :
            p.append(i)
            N //= i
            break
    else:
        if N > 1:
            p.append(N)
        break
    
for i in p:
    print(i)

#pass    