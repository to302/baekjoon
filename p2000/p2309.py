# coding=utf-8

'''일곱 난쟁이
https://www.acmicpc.net/problem/2309
'''

heights = []
for _ in range(9):
    heights.append(int(input()))

found = False
for i in range(8):
    for j in range(i+1, 9):
        jv = heights.pop(j)
        iv = heights.pop(i)
        if (sum(heights) == 100):
            found = True
            break
        else:
            heights.insert(i, iv)
            heights.insert(j, jv)
    if found:
        break

for n in sorted(heights):
    print(n)

# pass

# 브루트포스_알고리즘
# 정렬