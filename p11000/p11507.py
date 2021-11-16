# coding=utf-8

'''카드셋트
https://www.acmicpc.net/problem/11507
'''

s = input()

cs = {k:[1]*13 for k in 'PKHT'}

for i in range(0, len(s), 3):
    c = s[i:i+3]
    if cs[c[0]][int(c[1:])-1] == 0:
        print('GRESKA')
        break
    else:
        cs[c[0]][int(c[1:])-1] = 0
else:
    P, K, H, T = map(lambda x: sum(cs[x]), 'PKHT')
    print(P, K, H, T)

# pass

# 구현
# 자료구조
# 문자열
# 파싱
# 해시를 사용한 집합과 맵