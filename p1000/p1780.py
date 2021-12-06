# coding=utf-8

'''종이의 개수
https://www.acmicpc.net/problem/1780
'''

import sys
input = sys.stdin.readline

mat = []
for _ in range(int(input())):
    mat.append(list(map(int, input().split())))

def same_number(mat):
    num = mat[0][0]

    for r in mat:
        for c in r:
            if c != num:
                return False
    else:
        return True


def split_mat(mat):
    unit_len = len(mat) // 3
    nine_mats = []
    for i in range(3):
        bi = i*unit_len
        ei = bi + unit_len
        for j in range(3):
            bj = j * unit_len
            ej = bj + unit_len
            
            nine_mats.append([m[bj:ej] for m in mat[bi:ei]])
    return(nine_mats)


def solve(mat):
    global d
    if same_number(mat):
        d[mat[0][0]] += 1
    else:
        for m in split_mat(mat):
            solve(m)


d = {-1:0, 0:0, 1:0}

if __name__ == '__main__':
    solve(mat)
    print(d[-1])
    print(d[0])
    print(d[1])


# mat = [[0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 1, -1, 0, 1, -1], [0, -1, 1, 0, 1, -1, 0, 1, -1], [0, 1, -1, 1, 0, -1, 0, 1, -1]]
# mat2 = [i*3 for i in mat]*3

# pass but slow

# 분할 정복
# 재귀