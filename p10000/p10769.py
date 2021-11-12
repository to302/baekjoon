# coding=utf-8

'''행복한지 슬픈지
https://www.acmicpc.net/problem/10769
'''

arr = input().split(':-')
sad = 0
happy = 0
for t in arr[1:]:
    if t[0] == ')':
        happy += 1
    elif t[0] == '(':
        sad += 1

if happy == sad == 0 :
    print('none')
elif happy == sad != 0:
    print('unsure')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')

# pass

# 구현
# 문자열
# 파싱
