# coding=utf-8

'''콘서트
https://www.acmicpc.net/problem/16466
'''

N = int(input())

arr = sorted(map(int, input().split()))
if arr[0] != 1:
    print(1)
else:
    for i in range(len(arr)-1):
        if arr[i] + 1 != arr[i+1]:
            print(arr[i]+1)
            break
    else:
        print(arr[-1]+1)

# pass

# 구현
# 자료 구조
# 우선순위 큐
# from queue import PriorityQueue
# https://velog.io/@yeseolee/python-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90Priority-Queue