# coding=utf-8

# https://www.acmicpc.net/problem/2409
# 동혁건설에서는 이번에 새로운 건물을 짓게 되었다. 건물을 만들기 위해서는 짧은 길이의 강철 파이프가 N개 필요하다. 
# 마침 공사 때 사용하고 남은 긴 길이의 파이프가 M개 있어서 이를 먼저 사용한 뒤 필요한 파이프를 추가 주문하기로 하였다. 
# 동혁건설에서는 가급적이면 적은 개수의 파이프를 추가 주문하려 한다. 
# 즉, 주어진 강철 파이프를 잘라서 최대한 많은 개수의 필요한 파이프를 만들어 내려 한다.
# 작은 길이의 파이프를 만들기 위해서는 긴 길이의 파이프를 자르면 된다. 
# 자르는 과정에서 파이프의 길이에 손실이 있을 수도 있지만, 문제에서는 이를 무시해도 좋다. 
# 또한, 파이프를 자를 때에는 여러 번 자를 수도 있다.
# 입력
# 첫째 줄에 M(1≤M≤50)이 주어진다. 다음 줄에는 M개의 긴 강철 파이프의 길이가 주어진다. 
# 각각의 길이는 100,000을 넘지 않는 정수이다. 다음 줄에는 N(1≤N≤1023)이 주어진다. 
# 다음 줄에는 만들고자 하는 파이프의 길이를 나타내는 정수가 N개 주어진다. 
# 이 길이는 128 이하의 자연수이다.
# 출력
# 첫째 줄에 만들 수 있는 필요한 파이프의 최대 개수를 출력한다.

from sys import stdin

m = int(stdin.readline())
ml = sorted(list(map(int, stdin.readline().rstrip().split())))

n = int(stdin.readline())
nl = sorted(list(map(int, stdin.readline().rstrip().split())))

for i in range(len(ml)):
    if (ml[i] < nl[0]*2):
        mini = (min([ni - ml[i] for ni in nl if ni>=ml[i]]))
        nl.remove(ml[i]+mini)
        print(ml)
        print(nl)

    else:
        pass
    