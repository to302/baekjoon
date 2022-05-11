# coding=utf-8

'''수열

https://www.acmicpc.net/problem/2559
'''

N, K = map(int, input().split())
temp = list(map(int, input().split()))

ss = sum(temp[0:K])
mx = ss
for i in range(K,N):
    ss = ss - temp[i-K] + temp[i]
    if ss > mx:
        mx = ss
    
print(mx)


# pass

#누적 합
#두 포인터
#슬라이딩 윈도우