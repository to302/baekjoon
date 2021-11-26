# coding=utf-8

'''절대값 힙
https://www.acmicpc.net/problem/11286

관련
- 최소 힙: https://www.acmicpc.net/problem/1927
- 최대 힙: https://www.acmicpc.net/problem/11279

힙(heap)의 삽입 \n
    힙에 새로운 요소가 들어오면, 일단 새로운 노드를 힙의 마지막 노드에 이어서 삽입한다. \n
    새로운 노드를 부모 노드들과 교환해서 힙의 성질을 만족시킨다.            
    
힙(heap)의 삭제 \n 
    루트 노드 삭제하고 말단에 있는 노드를 루트 노드에 위치시킨 후, 규칙에 따라 아래 자식노드들과 교환하는 과정을 거친다.\n
    최소 heap 의 경우, 두 개의 자녀 중 더 작은 자녀를 비교기준으로 삼는다.

heapq 참고: https://www.daleseo.com/python-heapq/    
'''


import heapq
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    i = int(input())

    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(i), i))


    
# fail 

# 자료 구조
# 우선순위 큐
