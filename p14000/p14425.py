# coding=utf-8

'''문자열 집합
https://www.acmicpc.net/problem/14425
'''

def fn1():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())

    s = set()
    for _ in range(N):
        s.add(input().rstrip())

    cnt = 0
    for _ in range(M):
        w = input().rstrip()
        if w in s:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    fn1() # 트라이 구조 이용하지 않음.



# pass 

# 자료 구조
# 문자열
# 트리
# 트리를 사용한 집합과 맵
# 트라이(Trie)

