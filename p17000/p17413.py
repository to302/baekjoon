# coding=utf-8

'''단어 뒤집기 2
https://www.acmicpc.net/problem/17413
'''

s = input().rstrip()

in_tag = False
st = []
for c in s:
    if in_tag:
        print(c, end='')
        if c == '>':
            in_tag = False
    else:
        if c == '<':
            if len(st):
                print(''.join(reversed(st)), end='')
                st.clear()
            print(c, end='')
            in_tag = True
        elif c == ' ':
            if len(st):
                print(''.join(reversed(st)), end='')
                st.clear()
            print(c, end='')
        else:
            st.append(c)

if len(st):
    print(''.join(reversed(st)), end='')

# pass

# 구현
# 문자열

    