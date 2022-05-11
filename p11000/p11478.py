# coding=utf-8

'''서로 다른 부분 문자열의 개수

https://www.acmicpc.net/problem/11478
'''

s = input()
ss = set()
for i in range(1, len(s)+1):
    for j in range(len(s)):
        if len(s[j:j+i]) != i:
            break

        ss.add(s[j:j+i])

print(len(ss))


# pass

# 자료 구조
# 문자열
# 해시를 사용한 집합과 맵
# 트리를 사용한 집합과 맵