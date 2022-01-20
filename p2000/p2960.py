# coding=utf-8

'''에라토스테네스의 체
https://www.acmicpc.net/problem/2960

에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.
이 알고리즘은 다음과 같다.

1. 2부터 N까지 모든 정수를 적는다.
2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.
'''


n, k = map(int, input().split())

pn = [1 for _ in range(n+1)]
cnt = 0
for i in range(2, n+1):
    if cnt == k:
        break

    ii = i
    m = 1   
    while True:
        im = ii*m
        if im > n:
            break

        if pn[im] == 1:
            pn[im] = 0
            cnt += 1
        
        if cnt == k:
            print(im)
            break

        m += 1
        

# pass
            
# 수학
# 구현
# 정수론
# 소수 판정
# 에라토스테네스의 체



    
