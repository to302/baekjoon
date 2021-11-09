# coding=utf-8

'''백대열
https://www.acmicpc.net/problem/14490
'''

'''
유클리드 호제법(-互除法, Euclidean algorithm) 또는 유클리드 알고리즘은 2개의 자연수 또는 정식(整式)의 최대공약수를 구하는 알고리즘의 하나이다. 
호제법이란 말은 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘을 나타낸다. 
2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
'''

n, m = map(int, input().split(':'))

a, b = max(n, m), min(n, m)
while True:
    r = a % b
    if r == 0:
        break
    a = b
    b = r

print("{}:{}".format(int(n/b), int(m/b)))

# pass

# 수학
# 문자열
# 정수론
# 파싱
# 유클리드 호제법
