# coding=utf-8

'''30
https://www.acmicpc.net/problem/10610

배수 판정법
https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%88%98_%ED%8C%90%EC%A0%95%EB%B2%95
3의 배수는 각 자리 숫자의 합이 3의 배수인 수이다.
'''

ns = list(map(int, list(input().rstrip())))
try:
    ns.index(0)
    if sum(ns) % 3 == 0:
        ns.sort(reverse=True)
        print(''.join(map(str, ns)))
    else:
        print(-1)
except ValueError:
    print(-1)

# pass

# 수학
# 문자열
# 정렬
# 정수론
