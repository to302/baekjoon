# coding=utf-8

'''3의 배수
https://www.acmicpc.net/problem/1769'''

s = input().rstrip()

cnt = 0
while len(s)>1:
    s = str(sum(map(int, s)))
    cnt += 1
    
print(cnt)
if int(s) % 3 == 0:
    print("YES")
else:
    print("NO")

# pass

# 문자열
# 재귀
# 구현    