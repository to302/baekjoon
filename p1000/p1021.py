# coding=utf-8

# https://www.acmicpc.net/problem/1021
# 지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.
# 지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.
#   첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
#   왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
#   오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 
# 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 
# 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.
# 출력
# 첫째 줄에 문제의 정답을 출력한다.

class CircularQueue(list):
    
    def __init__(self, user_list):
        self._idx = 0
        self._move_cnt = 0
        self.extend(user_list) 
    
    def move_count(self):
        return self._move_cnt

    def left(self, m=1):
        self._idx = (self._idx + m) % len(self)
        self._move_cnt += m
    
    def right(self, m=1):
        self._idx = (self._idx - m + len(self)) % len(self)
        self._move_cnt += m

    def distance(self, v):
        diff = abs(self._idx - self.index(v))
        return min(diff, len(self) - diff)

    def get(self, v):
        v_idx = self.index(v)
        md = self.distance(v)
        if (self._idx < v_idx and v_idx-self._idx == md):
            self.left(md)
        else:
            self.right(md)

        if (self._idx >= len(self)-1):
            self._idx = 0
        self.pop(self._idx)


# m, n = map(int, input().split())
m, n = 50, 11 
cq = CircularQueue([i for i in range(1,m+1)])

# for i in map(int, input().split()):
for i in map(int, "45 2 23 6 7 40 10 30 12 14 49".split()):
    print(cq.distance(i), end="/")
    cq.get(i)
    print(i, cq)


print(cq.move_count())






