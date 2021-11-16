# coding=utf-8

'''파일 정리
https://www.acmicpc.net/problem/20291
'''

import sys
input = sys.stdin.readline

def fn1():
    out = dict()
    for _ in range(int(input())):
        ext = input().rstrip().split('.')[1]
        if ext in out.keys():
            out[ext] += 1
        else:
            out[ext] = 1

    for k in sorted(out.keys()):
        print(k, out[k])


if __name__ == '__main__':
    fn1()

# pass

# 구현
# 자료구조
# 문자열
# 정렬
# 파싱

