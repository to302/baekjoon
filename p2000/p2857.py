# coding=utf-8

'''FBI
https://www.acmicpc.net/problem/2857
'''

out = ''
for i in range(5):
    s = input()
    if s.find('FBI') != -1:
        out = out + str(i+1) + ' '

if out == '':
    print('HE GOT AWAY!')
else:
    print(out.rstrip())

# pass
# 
# 구현
# 문자열    