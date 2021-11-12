# coding=utf-8

'''8진수 2진수
https://www.acmicpc.net/problem/1212
'''

d = {
    '0':'000',
    '1':'001',
    '2':'010',
    '3':'011',
    '4':'100',
    '5':'101',
    '6':'110',
    '7':'111'
}
s = input()
ans = ''
for i in s:
    ans += d[i]

while ans[0] == '0' and len(ans)>1:
    ans = ans[1:]

print(ans)

# pass 

# 수학
# 구현
# 문자열
