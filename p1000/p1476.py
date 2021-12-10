# coding=utf-8

'''날짜 계산
https://www.acmicpc.net/problem/1476
'''

# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

E, S, M = map(int, input().split())

de, ds, dm = 1, 1, 1
lc = 1
while True:
    if de == E and ds == S and dm == M:
        print(lc)
        break
    
    lc += 1
    
    de = de+1 if de < 15 else de-14
    ds = ds+1 if ds < 28 else ds-27
    dm = dm+1 if dm < 19 else dm-18

    
# pass    

# 수학
# 구현
# 브루트포스 알고리즘
# 정수론
# 중국인의 나머지 정리