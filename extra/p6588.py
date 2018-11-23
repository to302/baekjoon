# -*- coding: utf-8 -*-

# 문제 : https://www.acmicpc.net/problem/6588
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
# 이 추측은 아직도 해결되지 않은 문제이다.
# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.
# == 입력 ==
# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.
# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
# 입력의 마지막 줄에는 0이 하나 주어진다.
# == 출력 ==
# 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 
# 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 
# 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

# 에라토스 테네스의 체 (소수 구하는 방식)
# 참고 : https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

class Eratos:

    def __init__(self, max_num):
        self.max_num = max_num
        self.prime_list_max = None  # 제약조건의 최대 소수 (≤ 1000000)
        

    def prime_list(self, n):
        # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
        sieve = [True] * n

        # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i] == True:           # i가 소수인 경우 
                for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                    sieve[j] = False

        # 소수 목록 산출
        return [i for i in range(2, n) if sieve[i] == True]


    def _prime_list_n(self, n):
        # 주어진 숫자에 대한 소수 목록을 반환
        if (self.prime_list_max == None):
            self.prime_list_max = self.prime_list(self.max_num)

        prime_list_n = self.prime_list_max
        for i in range(len(self.prime_list_max)):
            if self.prime_list_max[i] > n :
                prime_list_n = self.prime_list_max[:i]
                break    

        return prime_list_n

    def solve(self, n):
        pl = self._prime_list_n(n)
        for i in pl[:int(len(pl)/2)+1]:
            for j in reversed(pl):
                if (i+j == n):
                    print("{} = {} + {}".format(n, i, j))
                    return
                elif (i+j < n):
                    break

        print("Goldbach's conjecture is wrong.")

if __name__ == "__main__":
    nl = []
    while True:
        s = input()
        if s=='0':
            break
        else:
            nl.append(int(s))

    eratos = Eratos(1000000)
    for i in nl:
        eratos.solve(i)