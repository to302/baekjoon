# coding=utf-8

'''이항 계수 2
https://www.acmicpc.net/problem/11051
'''


from math import factorial

N, K = map(int, input().split())

def fn1(N, K):
    print( (factorial(N) // (factorial(K) * factorial(N-K))) % 10007 )


arr = [[ 0 for _ in range(1001) ] for _ in range(1001) ]
def fn2(n, k):
    if n == k or k == 0:
        arr[n][k] = 1
        return 1
    print(arr[n][k])
    if arr[n][k] == 0:
        arr[n][k] = (fn2(n-1, k-1) + fn2(n-1, k)) % 10007
    return(arr[n][k])




if __name__ == '__main__':
    # fn1()
    print(fn2(N, K))
    
# pass - fn1



# 수학
# 다이나믹 프로그래밍
# 조합론


'''
input : 1000 500
output : 8662
ans : 5418

input : 100 50
output : 3590
ans : 9219

R_N/R_K를 R_N//R_K로 고치니 정답이네요
큰 수 int 변환과정에서 오류가 발생하는 것 같습니다.

또 이 문제의 의도는 단순히 조합 계산을 통해 푸는 것이 아니라 조합의 성질을 이용한 메모이제이션을 사용하는 것이니
이점에 대해서도 생각해보시면 좋을 것 같습니다.

메모이제이션(memoization)은 컴퓨터 프로그램이 동일한 계산을 반복해야 할 때, 
이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술이다.
'''