# coding=utf-8

'''숫자놀이
https://www.acmicpc.net/problem/1755
'''

M, N = map(int, input().split())

ns = ['zero','one','two','three', 'four','five','six','seven','eight','nine']
arr = []
for i in range(M, N+1):
    i1 = '' if i//10 == 0 else str(ns[i//10]) + ' '
    i2 = ns[i%10]
    arr.append( (f'{i1}{i2}', i) )
    
arr.sort()

# 한 줄에 10개씩 출력한다
idx = 1
for i1, i2 in arr:
    print(i2, end=' ')
    if idx % 10 == 0:
        print()

    idx += 1


# pass


# 수학
# 문자열
# 정렬