# coding=utf-8

'''TV 크기
https://www.acmicpc.net/problem/1297

실제 TV의 높이나 너비가 소수점이 나올 경우에는 그 수보다 작으면서 가장 큰 정수로 출력한다. (예) 1.7 -> 1
'''

D, H, W = map(int, input().split())

a = (D**2 / (H**2 + W**2))**0.5
print(int(a*H//1), int(a*W//1))

# pass


# 수학
# 기하학
# 피타고라스 정리
