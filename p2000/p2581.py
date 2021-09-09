# coding=utf-8

'''소수
https://www.acmicpc.net/problem/2581
소수: 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수

M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
'''

M = int(input())
N = int(input())

p = []
for i in range(max(M,2), N+1):
    for j in range(2, int(i ** 0.5)+1):
        if (i % j == 0):
            break
    else:        
        p.append(i)

if len(p)==0:
    print(-1)
else:
    print(sum(p))
    print(min(p))


'''for else 구문
for와 함께 쓰는 else는, for문이 중간에 break 등으로 끊기지 않고,
끝까지 수행 되었을 때 수행하는 코드를 담고 있습니다.
'''

#pass