# coding=utf-8

'''ROT13
https://www.acmicpc.net/problem/11655
'''

s = input()

UA = ord('A')
UZ = ord('Z')
LA = ord('a')
LZ = ord('z')

out = ''
for c in s:
    oc = ord(c)
    if UA <= oc <= UZ:
        if oc + 13 > UZ:
            oc = oc + 13 - UZ + UA - 1
        else:
            oc = oc + 13
        out += chr(oc)
    elif LA <= oc <= LZ:
        if oc + 13 > LZ:
            oc = oc + 13 - LZ + LA - 1
        else:
            oc = oc + 13
        out += chr(oc)
    else:
        out += c
    
print(out)


# pass

# 문자열
# 구현
