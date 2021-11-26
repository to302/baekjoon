# coding=utf-8

'''최대 힙
https://www.acmicpc.net/problem/11279

관련
- 최소 힙: https://www.acmicpc.net/problem/1927
- 절댓값 힙: https://www.acmicpc.net/problem/11286

힙(heap)의 삽입 \n
    힙에 새로운 요소가 들어오면, 일단 새로운 노드를 힙의 마지막 노드에 이어서 삽입한다. \n
    새로운 노드를 부모 노드들과 교환해서 힙의 성질을 만족시킨다.            
    
힙(heap)의 삭제 \n 
    루트 노드 삭제하고 말단에 있는 노드를 루트 노드에 위치시킨 후, 규칙에 따라 아래 자식노드들과 교환하는 과정을 거친다.\n
    최소 heap 의 경우, 두 개의 자녀 중 더 작은 자녀를 비교기준으로 삼는다.
'''

class MaxHeap():
    '''최대 힙'''

    def __init__(self):
        self.heap = [0] # heap은 인덱스 1부터 시작
        
    def insert(self, i):
        self.heap.append(i)
        
        idx = len(self.heap) - 1
        while True:
            pidx = idx // 2
            if pidx == 0:
                break

            if self.heap[pidx] < self.heap[idx]:
                tmp = self.heap[pidx]
                self.heap[pidx] = self.heap[idx]
                self.heap[idx] = tmp
                idx = pidx
            else:
                break
        

    def print(self, id='>> '):
        print(id, self.heap)


    def delete(self):
        if len(self.heap) == 1:
            print(0)
            return(0)
        
        print(self.heap[1])
        if len(self.heap) > 2:
            self.heap[1] = self.heap.pop()
        else:
            del self.heap[1]

        idx = 1
        while True:
            cidx = (idx*2, idx*2 + 1)
            i1, i2 = None, None
            if len(self.heap) - 1 >= cidx[0]:
                i1 = cidx[0]
            if len(self.heap) - 1 >= cidx[1]:
                i2 = cidx[1]
            
            if i1 == None and i2 == None:
                break
            else:
                if i2 == None:
                    si = i1
                else:
                    si = i1 if self.heap[i1] >= self.heap[i2] else i2

                if self.heap[idx] < self.heap[si]:
                    tmp = self.heap[idx]
                    self.heap[idx] = self.heap[si]
                    self.heap[si] = tmp
                    idx = si
                else:
                    break

heap = MaxHeap()

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    i = int(input())
    if i == 0:
        heap.delete()
    else:
        heap.insert(i)


# pass

# 자료구조
# 우선순위 큐
