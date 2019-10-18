# coding=utf-8

"""
https://www.acmicpc.net/problem/5586
JOI와 IOI

문제
입력으로 주어지는 문자열에서 연속으로 3개의 문자가 JOI 또는 IOI인 곳이 각각 몇 개 있는지 구하는 프로그램을 작성하시오. 
문자열을 알파벳 대문자로만 이루어져 있다. 예를 들어, 아래와 같이 "JOIOIOI"에는 JOI가 1개, IOI가 2개 있다.

입력
첫째 줄에 알파벳 10000자 이내의 문자열이 주어진다. 

출력
첫째 줄에 문자열에 포함되어 있는 JOI의 개수, 둘째 줄에 IOI의 개수를 출력한다.
"""

s = str(input())
nj = 0
ni = 0
for i in range(len(s)-2):
    if (s[i:i+3] == "JOI"):
        nj += 1
    elif (s[i:i+3] == "IOI"):
        ni += 1

print(nj, ni, sep="\n")

# pass(2019-10-18)