# coding=utf-8

'''수 정렬하기 3
https://www.acmicpc.net/problem/10989

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''


# 입력값 전체의 정렬은 메모리 초과로 나온다.


import sys
input = sys.stdin.readline

dic = dict() # <-- 여기를 배열 10001 로 하는 것이 좀 더 빠른 듯..
for _ in range(int(input())):
    i = int(input().rstrip())
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
    
for k in sorted(dic.keys()):
    for _ in range(dic[k]):
        print(k)
    
    

# pass

# 정렬    
