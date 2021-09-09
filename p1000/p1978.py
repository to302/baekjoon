# coding=utf-8

'''소수 찾기
https://www.acmicpc.net/problem/1978
소수: 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수
수학에서 에라토스테네스의 체는 소수를 찾는 방법이다. 고대 그리스 수학자 에라토스테네스가 발견하였다.
https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
'''

N = int(input())
Ns = list(map(int, input().split())) # 수는 1,000 이하의 자연수

def prime_list(n):
    sieve  = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]


pl = prime_list(1000)
print(sum([1 for i in Ns if i in pl ]))

#pass
