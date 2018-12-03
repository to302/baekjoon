# coding=utf-8

# https://www.acmicpc.net/problem/11050
# 재귀함수로 이항계수를 구해봅시다.
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 nCk 를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)
# 출력
# nCk 를 출력한다.



def mul(n,k):
    if (k==0):
        return 1
    if (k>0):
        return n*mul(n-1, k-1)
        
    return n
    
n, k = map(int, input().split())
print(int(mul(n,k) / mul(k,k)))
