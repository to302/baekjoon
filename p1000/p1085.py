# coding=utf-8

'''직사각형에서 탈출
https://www.acmicpc.net/problem/1085

한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 x, y, w, h가 주어진다.
첫째 줄에 문제의 정답을 출력한다.

1 ≤ w, h ≤ 1,000
1 ≤ x ≤ w-1
1 ≤ y ≤ h-1
x, y, w, h는 정수
'''

x, y, w, h = map(int, input().split())
print(min(w-x, h-y, y, x))

#pass