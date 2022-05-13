# coding=utf-8

'''오큰수
https://www.acmicpc.net/problem/17298

골드4
'''

from collections import deque

N = int(input())
q = list(map(int, input().split()))
result = [-1] * N

stack = deque()

for i in range(N-1, -1, -1):
    while len(stack)>0:
        if stack[-1] > q[i]:
            result[i] = stack[-1]
            stack.append(q[i])
            break
        else:
            stack.pop()
    else:
        stack.append(q[i])
        
# print(' '.join(map(str, result)))
print(*result)


# pass

# 자료구조
# 스택


'''
질문자님의 코드를 보면 왼쪽부터 원소를 하나씩 꺼내면서 남은 원소를 모두 확인하는 O(n^2)로 동작하게 됩니다. (입력이 내림차순으로 정렬된 경우를 생각해보세요)
하지만 오른쪽원소부터 확인하며 스택을 이용하는 경우를 보면 시간복잡도가 O(n) 입니다.
https://www.acmicpc.net/board/view/74909
의 답변이 참고가 될 것 같습니다.
'''

                



    

    
    
    




    
    


#자료구조 #스택

