# coding=utf-8

'''뒤집힌 덧셈
https://www.acmicpc.net/problem/1357
'''

'''
# 문자열 뒤집기
## slice를 이용한 방법(python 3.*)
slice에서 각각의 항목은 [start:stop:step]를 의미합니다.   
string[::-1]처럼 반대 방향으로 리스트의 데이터를 자를 수 있습니다.  

## reversed()를 이용한 방법
string = 'Hello, World!'  
reversed_str = "".join(reversed(string))  
'''

def Rev(x:str) -> int:
    return int(x[::-1])

X, Y = input().rstrip().split()
print(Rev(str(Rev(X) + Rev(Y))))

# pass  

# 구현
# 문자열
